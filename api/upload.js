import axios from 'axios';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const body = JSON.parse(req.body || '{}');
    const { videoBase64, assemblyAIKey } = body;

    if (!videoBase64 || !assemblyAIKey) {
      return res.status(400).json({ 
        error: 'Video data and API key required',
        success: false 
      });
    }

    console.log('Uploading to AssemblyAI...');

    // Base64를 Buffer로 변환
    const videoBuffer = Buffer.from(videoBase64, 'base64');

    // AssemblyAI에 업로드
    const response = await axios.post(
      'https://api.assemblyai.com/v2/upload',
      videoBuffer,
      {
        headers: {
          'authorization': assemblyAIKey,
          'content-type': 'application/octet-stream',
        },
        maxBodyLength: Infinity,
        maxContentLength: Infinity
      }
    );

    console.log('Upload successful:', response.data);

    return res.status(200).json({
      success: true,
      url: response.data.upload_url,
      message: 'Video uploaded successfully'
    });

  } catch (error) {
    console.error('Upload error:', error.message);
    return res.status(500).json({ 
      error: 'Upload failed',
      details: error.response?.data || error.message,
      success: false
    });
  }
}
