import OpenAI from 'openai';

export const config = {
  api: {
    bodyParser: true,
  },
};

export default async function handler(req, res) {
  // CORS 헤더 추가
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // 요청 본문 로깅 (디버깅용)
  console.log('Request body:', req.body);

  const { text, openAIKey } = req.body;

  if (!text || !openAIKey) {
    console.error('Missing params - text:', !!text, 'openAIKey:', !!openAIKey);
    return res.status(400).json({ 
      success: false,
      error: 'Text and API key are required',
      received: {
        hasText: !!text,
        hasOpenAIKey: !!openAIKey
      }
    });
  }

  try {
    const openai = new OpenAI({
      apiKey: openAIKey,
    });

    const completion = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: [
        {
          role: 'system',
          content: `You are a professional Japanese to Korean translator. 
Translate the following Japanese drama dialogue to natural Korean. 
Keep the emotional tone and nuance of the original dialogue.
Only provide the translation without any explanations.`
        },
        {
          role: 'user',
          content: text
        }
      ],
      temperature: 0.3,
    });

    const translatedText = completion.choices[0].message.content.trim();

    return res.status(200).json({
      success: true,
      translatedText,
      originalText: text,
      message: 'Translation completed'
    });
  } catch (error) {
    console.error('Translation error:', error.message);
    return res.status(500).json({
      success: false,
      error: 'Translation failed',
      details: error.message
    });
  }
}
