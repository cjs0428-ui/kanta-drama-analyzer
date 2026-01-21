import https from 'https';

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
    let body = '';
    
    // 데이터 수신
    req.on('data', chunk => {
      body += chunk.toString();
    });

    req.on('end', async () => {
      try {
        const { videoBase64, assemblyAIKey } = JSON.parse(body);

        if (!videoBase64 || !assemblyAIKey) {
          return res.status(400).json({ error: 'Video data and API key required' });
        }

        // Base64를 Buffer로 변환
        const videoBuffer = Buffer.from(videoBase64, 'base64');

        // AssemblyAI에 업로드
        const uploadUrl = await uploadToAssemblyAI(videoBuffer, assemblyAIKey);

        return res.status(200).json({
          success: true,
          url: uploadUrl,
          message: 'Video uploaded successfully'
        });

      } catch (parseError) {
        console.error('Parse error:', parseError);
        return res.status(400).json({ error: 'Invalid request data' });
      }
    });

  } catch (error) {
    console.error('Upload error:', error);
    return res.status(500).json({ 
      error: 'Internal server error',
      details: error.message 
    });
  }
}

// AssemblyAI 업로드 헬퍼 함수
function uploadToAssemblyAI(buffer, apiKey) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.assemblyai.com',
      path: '/v2/upload',
      method: 'POST',
      headers: {
        'authorization': apiKey,
        'content-type': 'application/octet-stream',
        'content-length': buffer.length
      }
    };

    const req = https.request(options, (response) => {
      let data = '';

      response.on('data', (chunk) => {
        data += chunk;
      });

      response.on('end', () => {
        if (response.statusCode === 200) {
          const result = JSON.parse(data);
          resolve(result.upload_url);
        } else {
          reject(new Error(`Upload failed: ${response.statusCode} ${data}`));
        }
      });
    });

    req.on('error', (error) => {
      reject(error);
    });

    req.write(buffer);
    req.end();
  });
}
