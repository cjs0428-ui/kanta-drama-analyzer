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
      error: 'Translation failed',
      details: error.message
    });
  }
}
