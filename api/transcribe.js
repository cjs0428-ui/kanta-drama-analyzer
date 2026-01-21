import axios from 'axios';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { videoUrl, assemblyAIKey } = req.body;

  if (!videoUrl || !assemblyAIKey) {
    return res.status(400).json({ error: 'Video URL and API key are required' });
  }

  try {
    const response = await axios.post(
      'https://api.assemblyai.com/v2/transcript',
      {
        audio_url: videoUrl,
        language_code: 'ja',
        speech_model: 'best',
      },
      {
        headers: {
          authorization: assemblyAIKey,
          'content-type': 'application/json',
        },
      }
    );

    const transcriptionId = response.data.id;

    return res.status(200).json({
      success: true,
      transcriptionId,
      status: 'processing',
      message: 'Transcription started'
    });

  } catch (error) {
    console.error('Transcription error:', error.response?.data || error.message);
    return res.status(500).json({
      error: 'Transcription failed',
      details: error.response?.data || error.message
    });
  }
}
