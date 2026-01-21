import axios from 'axios';

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { id, assemblyAIKey } = req.query;

  if (!id || !assemblyAIKey) {
    return res.status(400).json({ error: 'Transcription ID and API key are required' });
  }

  try {
    const response = await axios.get(
      `https://api.assemblyai.com/v2/transcript/${id}`,
      {
        headers: {
          authorization: assemblyAIKey,
        },
      }
    );

    const { status, text, error } = response.data;

    if (status === 'completed') {
      return res.status(200).json({
        success: true,
        status: 'completed',
        text: text || '',
        message: 'Transcription completed'
      });
    } else if (status === 'error') {
      return res.status(500).json({
        success: false,
        status: 'error',
        error: error || 'Transcription failed',
      });
    } else {
      return res.status(200).json({
        success: true,
        status: status,
        message: 'Transcription in progress'
      });
    }

  } catch (error) {
    console.error('Status check error:', error.response?.data || error.message);
    return res.status(500).json({
      error: 'Failed to check status',
      details: error.response?.data || error.message
    });
  }
}
