import { put } from '@vercel/blob';

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    // Vercel Blob에 업로드
    const blob = await put(
      `video-${Date.now()}.mp4`,
      req,
      {
        access: 'public',
        token: process.env.BLOB_READ_WRITE_TOKEN,
      }
    );

    console.log('✅ Vercel Blob 업로드 성공:', blob.url);

    // AssemblyAI로 전달
    const { assemblyAIKey } = req.query;

    if (!assemblyAIKey) {
      return res.status(400).json({ 
        error: 'AssemblyAI key required',
        success: false 
      });
    }

    const response = await fetch('https://api.assemblyai.com/v2/transcript', {
      method: 'POST',
      headers: {
        'authorization': assemblyAIKey,
        'content-type': 'application/json',
      },
      body: JSON.stringify({
        audio_url: blob.url,
        language_code: 'ja',
        speech_model: 'best',
      }),
    });

    const data = await response.json();

    return res.status(200).json({
      success: true,
      blobUrl: blob.url,
      transcriptionId: data.id,
      message: 'Upload and transcription started'
    });

  } catch (error) {
    console.error('❌ 업로드 에러:', error);
    return res.status(500).json({ 
      error: 'Upload failed',
      details: error.message,
      success: false
    });
  }
}
