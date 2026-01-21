import OpenAI from 'openai';

export const config = {
  api: {
    bodyParser: true,
  },
};

export default async function handler(req, res) {
  // CORS 헤더
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method not allowed' });
  }

  const { episodes, overallStory, criteria, openAIKey } = req.body;

  console.log('Received data:', { 
    episodeCount: episodes?.length, 
    hasOverallStory: !!overallStory,
    criteria,
    hasKey: !!openAIKey 
  });

  if (!episodes || !overallStory || !criteria || !openAIKey) {
    return res.status(400).json({ 
      success: false,
      error: 'Episodes, overall story, criteria, and API key are required',
      received: {
        hasEpisodes: !!episodes,
        hasOverallStory: !!overallStory,
        hasCriteria: !!criteria,
        hasOpenAIKey: !!openAIKey
      }
    });
  }

  try {
    const openai = new OpenAI({
      apiKey: openAIKey,
    });

    const { 
      targetAge, 
      tone, 
      platform, 
      length, 
      keyword,
      additionalRequirements,
      logicType = '결과(정량)를 먼저 보여준 뒤, 원인으로 돌아가 시사를 제공하여 공감을 유발'
    } = criteria;

    // 회차별 스토리 요약
    const episodeSummaries = episodes.map(ep => 
      `[${ep.episode}회차] ${ep.korean.substring(0, 200)}...`
    ).join('\n\n');

    // 일본어 광고 문구 생성
    const japaneseCompletion = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: [
        {
          role: 'system',
          content: `あなたは日本のショートドラマ専門のクリエイティブコピーライターです。

【広告文の条件】
- ターゲット年齢: ${targetAge}
- トーン: ${tone}
- プラットフォーム: ${platform}
- 長さ: ${length}
${keyword ? `- キーワード: ${keyword}` : ''}

【論理構造】
${logicType}

【追加要件】
${additionalRequirements || 'なし'}

【重要】
- 動画素材に入れるナレーションとして自然な日本語で作成
- ストーリーの核心を突く感情的なフックを作る
- ${tone}のトーンを徹底的に守る
- ハッシュタグは使わない（動画素材用）
- 視聴者が「続きが気になる」「見たい」と思わせる
- 絵文字は控えめに、あれば1-2個程度

広告文のみを出力してください。説明は不要です。`
        },
        {
          role: 'user',
          content: `【ドラマストーリー全体分析】
${overallStory}

【各話の内容】
${episodeSummaries}

上記の内容をもとに、${platform}用の魅力的な広告文を作成してください。`
        }
      ],
      temperature: 0.8,
      max_tokens: 500
    });

    const japaneseAd = japaneseCompletion.choices[0].message.content.trim();

    // 한국어 번역
    const koreanCompletion = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: [
        {
          role: 'system',
          content: `당신은 전문 일본어-한국어 번역가입니다.
다음 일본어 광고 문구를 자연스러운 한국어로 번역하세요.
- 감성과 뉘앙스를 그대로 유지
- 한국 시청자에게 자연스럽게 들리도록
- 설명 없이 번역문만 제공`
        },
        {
          role: 'user',
          content: japaneseAd
        }
      ],
      temperature: 0.3,
      max_tokens: 500
    });

    const koreanAd = koreanCompletion.choices[0].message.content.trim();

    console.log('Ad copy generated successfully');

    return res.status(200).json({
      success: true,
      japaneseAd,
      koreanAd,
      criteria,
      message: 'Ad copy generated successfully'
    });

  } catch (error) {
    console.error('Ad generation error:', error.message);
    return res.status(500).json({
      success: false,
      error: 'Ad copy generation failed',
      details: error.message
    });
  }
}
