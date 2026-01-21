import OpenAI from 'openai';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { text, openAIKey } = req.body;

  if (!text || !openAIKey) {
    return res.status(400).json({ error: 'Text and API key are required' });
  }

  try {
    const openai = new OpenAI({
      apiKey: openAIKey,
    });

    const completion = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        {
          role: 'system',
          content: `You are a professional drama story analyst. 
Analyze the following Korean drama dialogue and provide:
1. Genre (장르)
2. Main emotions (주요 감정)
3. Plot summary (줄거리 요약)
4. Key points (핵심 포인트)
5. Target audience (타겟층)
6. Emotional keywords (감성 키워드)

Format your response in Korean with clear sections using emojis.`
        },
        {
          role: 'user',
          content: `다음 드라마 대사를 분석해주세요:\n\n${text}`
        }
      ],
      temperature: 0.7,
    });

    const analysis = completion.choices[0].message.content.trim();

    return res.status(200).json({
      success: true,
      analysis,
      message: 'Story analysis completed'
    });

  } catch (error) {
    console.error('Analysis error:', error.message);
    return res.status(500).json({
      error: 'Story analysis failed',
      details: error.message
    });
  }
}
