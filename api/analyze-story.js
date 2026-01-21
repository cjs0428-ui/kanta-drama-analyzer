import OpenAI from 'openai';

export const config = {
  api: {
    bodyParser: true,
  },
  maxDuration: 60, // Vercel Pro 플랜이면 60초, 무료는 10초
};

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method not allowed' });
  }

  const { episodes, openAIKey } = req.body;

  console.log('Received data:', { episodeCount: episodes?.length, hasKey: !!openAIKey });

  if (!episodes || !openAIKey) {
    return res.status(400).json({ 
      success: false,
      error: 'Episodes and API key are required',
      received: {
        hasEpisodes: !!episodes,
        hasOpenAIKey: !!openAIKey
      }
    });
  }

  try {
    const openai = new OpenAI({
      apiKey: openAIKey,
    });

    console.log('Starting analysis...');

    // 🔥 병렬 처리로 회차별 분석 속도 향상
    const episodeAnalysisPromises = episodes.map(async (ep) => {
      console.log(`Analyzing episode ${ep.episode}...`);
      
      try {
        const completion = await openai.chat.completions.create({
          model: 'gpt-4o-mini',
          messages: [
            {
              role: 'system',
              content: `당신은 전문 드라마 스토리 분석가입니다. 
주어진 회차의 대사를 분석하여 다음을 제공하세요:
- 이 회차의 핵심 사건
- 등장인물의 관계 변화
- 감정선
- 중요한 대사나 장면

간단명료하게 한국어로 작성하세요.`
            },
            {
              role: 'user',
              content: `${ep.episode}회차 대사:\n\n${ep.korean}`
            }
          ],
          temperature: 0.7,
          max_tokens: 400
        });
        
        return {
          episode: ep.episode,
          analysis: completion.choices[0].message.content.trim()
        };
      } catch (error) {
        console.error(`Episode ${ep.episode} analysis failed:`, error.message);
        return {
          episode: ep.episode,
          analysis: `분석 실패: ${error.message}`
        };
      }
    });

    // 모든 회차 병렬 분석
    const episodeAnalysis = await Promise.all(episodeAnalysisPromises);

    console.log('Episode analyses completed, starting overall analysis...');

    // 전체 스토리 분석 (텍스트 길이 제한)
    const allText = episodes.map(ep => {
      // 각 회차당 최대 300자로 제한
      const truncated = ep.korean.substring(0, 300);
      return `[${ep.episode}회차]\n${truncated}${ep.korean.length > 300 ? '...' : ''}`;
    }).join('\n\n');
    
    const overallCompletion = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: [
        {
          role: 'system',
          content: `당신은 전문 드라마 스토리 분석가입니다.
전체 회차를 종합하여 다음을 분석하세요:

📌 **전체 줄거리 요약**
- 스토리의 시작, 전개, 절정을 간단히 요약

🎭 **주요 테마**
- 이 드라마가 다루는 핵심 주제

💕 **감정선**
- 전체적인 감정의 흐름

🎯 **타겟 관객**
- 어떤 사람들이 좋아할지

✨ **매력 포인트**
- 이 드라마의 가장 큰 매력

각 섹션을 이모지와 함께 명확하게 구분하여 한국어로 작성하세요.`
        },
        {
          role: 'user',
          content: `다음은 숏드라마 전체 회차의 대사입니다:\n\n${allText}`
        }
      ],
      temperature: 0.7,
      max_tokens: 800
    });

    const overallAnalysis = overallCompletion.choices[0].message.content.trim();

    console.log('Analysis completed successfully');

    return res.status(200).json({
      success: true,
      episodeAnalysis,
      overallAnalysis,
      message: 'Story analysis completed'
    });

  } catch (error) {
    console.error('Analysis error:', error.message);
    return res.status(500).json({
      success: false,
      error: 'Story analysis failed',
      details: error.message
    });
  }
}
