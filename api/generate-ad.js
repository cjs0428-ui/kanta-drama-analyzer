import OpenAI from 'openai';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { story, analysis, criteria, openAIKey } = req.body;

  if (!story || !criteria || !openAIKey) {
    return res.status(400).json({ error: 'Story, criteria, and API key are required' });
  }

  try {
    const openai = new OpenAI({
      apiKey: openAIKey,
    });

    const { targetAge, tone, platform, length, keyword } = criteria;

    const systemPrompt = `You are a creative copywriter specializing in drama marketing.
Create a compelling ad copy for a Japanese drama based on the story and analysis provided.

Ad Criteria:
- Target Age: ${targetAge}
- Tone: ${tone}
- Platform: ${platform}
- Length: ${length}
${keyword ? `- Keywords to include: ${keyword}` : ''}

Requirements:
- Make it attention-grabbing and emotional
- Use appropriate emojis
- Include relevant hashtags
- Match the tone specified (${tone})
- Keep it natural and conversational in Korean
- Create urgency or curiosity to watch

Provide ONLY the final ad copy without explanations.`;

    const completion = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        {
          role: 'system',
          content: systemPrompt
        },
        {
          role: 'user',
          content: `Story:\n${story}\n\nAnalysis:\n${analysis || 'No analysis provided'}`
        }
      ],
      temperature: 0.8,
    });

    const adCopy = completion.choices[0].message.content.trim();

    return res.status(200).json({
      success: true,
      adCopy,
      criteria,
      message: 'Ad copy generated successfully'
    });

  } catch (error) {
    console.error('Ad generation error:', error.message);
    return res.status(500).json({
      error: 'Ad copy generation failed',
      details: error.message
    });
  }
}
