const { useState } = React;

function App() {
  const [apiKeys, setApiKeys] = useState({
    assemblyAI: '',
    openAI: ''
  });
  const [step, setStep] = useState(0);
  const [videoFile, setVideoFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [transcribing, setTranscribing] = useState(false);
  const [translating, setTranslating] = useState(false);
  const [analyzing, setAnalyzing] = useState(false);
  const [generatingAd, setGeneratingAd] = useState(false);
  
  const [japaneseText, setJapaneseText] = useState('');
  const [koreanText, setKoreanText] = useState('');
  const [storyAnalysis, setStoryAnalysis] = useState('');
  const [adCopy, setAdCopy] = useState('');
  
  const [adCriteria, setAdCriteria] = useState({
    targetAge: '20-30대',
    tone: '감성적',
    platform: '인스타그램',
    length: '짧게 (1-2줄)',
    keyword: ''
  });

  const handleSaveKeys = () => {
    if (!apiKeys.assemblyAI.trim() || !apiKeys.openAI.trim()) {
      alert('두 개의 API 키를 모두 입력해주세요.');
      return;
    }
    setStep(1);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type.startsWith('video/')) {
      setVideoFile(file);
    } else {
      alert('비디오 파일만 업로드 가능합니다.');
    }
  };

  const handleUpload = async () => {
    if (!videoFile) {
      alert('파일을 선택해주세요.');
      return;
    }

    if (videoFile.size > 500 * 1024 * 1024) {
      alert('파일이 너무 큽니다. 500MB 이하의 영상을 선택해주세요.');
      return;
    }

    setUploading(true);
    try {
      console.log('📤 파일 업로드 시작:', videoFile.name, '크기:', (videoFile.size / 1024 / 1024).toFixed(2) + 'MB');
      
      const arrayBuffer = await videoFile.arrayBuffer();
      console.log('✅ ArrayBuffer 생성 완료');
      
      console.log('🚀 AssemblyAI로 업로드 중...');
      const uploadResponse = await fetch('https://api.assemblyai.com/v2/upload', {
        method: 'POST',
        headers: {
          'authorization': apiKeys.assemblyAI,
        },
        body: arrayBuffer
      });

      console.log('📊 업로드 응답 상태:', uploadResponse.status);

      if (!uploadResponse.ok) {
        const errorText = await uploadResponse.text();
        throw new Error(`업로드 실패 (${uploadResponse.status}): ${errorText}`);
      }

      const uploadData = await uploadResponse.json();
      console.log('✅ 업로드 성공! URL:', uploadData.upload_url);
      
      setStep(2);
      handleTranscribe(uploadData.upload_url);
    } catch (error) {
      console.error('❌ 업로드 에러:', error);
      alert('업로드 실패: ' + error.message);
    } finally {
      setUploading(false);
    }
  };

  const handleTranscribe = async (videoUrl) => {
    setTranscribing(true);
    try {
      const response = await fetch('/api/transcribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          videoUrl,
          assemblyAIKey: apiKeys.assemblyAI
        })
      });
      
      const data = await response.json();
      if (!data.success) throw new Error(data.error);
      
      checkTranscriptionStatus(data.transcriptionId);
    } catch (error) {
      alert('음성 인식 실패: ' + error.message);
      setTranscribing(false);
    }
  };

  const checkTranscriptionStatus = async (id) => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch(`/api/status?id=${id}&assemblyAIKey=${apiKeys.assemblyAI}`);
        const data = await response.json();
        
        if (data.status === 'completed') {
          clearInterval(interval);
          setJapaneseText(data.text);
          setTranscribing(false);
          setStep(3);
          handleTranslate(data.text);
        } else if (data.status === 'error') {
          clearInterval(interval);
          setTranscribing(false);
          alert('음성 인식 실패');
        }
      } catch (error) {
        clearInterval(interval);
        setTranscribing(false);
      }
    }, 3000);
  };

  const handleTranslate = async (text) => {
    setTranslating(true);
    try {
      const response = await fetch('/api/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          text,
          openAIKey: apiKeys.openAI
        })
      });
      
      const data = await response.json();
      if (!data.success) throw new Error(data.error);
      
      setKoreanText(data.translatedText);
      setStep(4);
    } catch (error) {
      alert('번역 실패: ' + error.message);
    } finally {
      setTranslating(false);
    }
  };

  const handleAnalyzeStory = async () => {
    setAnalyzing(true);
    try {
      const response = await fetch('/api/analyze-story', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          text: koreanText,
          openAIKey: apiKeys.openAI
        })
      });
      
      const data = await response.json();
      if (!data.success) throw new Error(data.error);
      
      setStoryAnalysis(data.analysis);
      setStep(5);
    } catch (error) {
      alert('분석 실패: ' + error.message);
    } finally {
      setAnalyzing(false);
    }
  };

  const handleGenerateAd = async () => {
    setGeneratingAd(true);
    try {
      const response = await fetch('/api/generate-ad', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          story: koreanText,
          analysis: storyAnalysis,
          criteria: adCriteria,
          openAIKey: apiKeys.openAI
        })
      });
      
      const data = await response.json();
      if (!data.success) throw new Error(data.error);
      
      setAdCopy(data.adCopy);
      setStep(6);
    } catch (error) {
      alert('광고 생성 실패: ' + error.message);
    } finally {
      setGeneratingAd(false);
    }
  };

  return React.createElement('div', { className: "min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 p-6" },
    React.createElement('div', { className: "max-w-6xl mx-auto" },
      React.createElement('div', { className: "text-center mb-8" },
        React.createElement('h1', { className: "text-4xl font-bold text-gray-800 mb-2" }, '🎬 KANTA 숏드라마 분석기'),
        React.createElement('p', { className: "text-gray-600" }, '일본 드라마 대사를 자동으로 번역하고 분석해서 광고 문구를 만들어드립니다')
      ),
      
      step === 0 && React.createElement('div', { className: "bg-white rounded-lg shadow-lg p-8" },
        React.createElement('h2', { className: "text-2xl font-bold mb-6" }, '🔑 API 키 설정'),
        React.createElement('div', { className: "bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6" },
          React.createElement('p', { className: "text-sm text-blue-800 font-medium mb-2" }, '서비스 이용을 위해 API 키가 필요합니다')
        ),
        React.createElement('div', { className: "space-y-6" },
          React.createElement('div', null,
            React.createElement('label', { className: "block text-sm font-medium mb-2" }, 'AssemblyAI API Key'),
            React.createElement('input', {
              type: 'password',
              value: apiKeys.assemblyAI,
              onChange: (e) => setApiKeys({...apiKeys, assemblyAI: e.target.value}),
              placeholder: 'AssemblyAI API 키',
              className: "w-full border rounded-lg p-3"
            })
          ),
          React.createElement('div', null,
            React.createElement('label', { className: "block text-sm font-medium mb-2" }, 'OpenAI API Key'),
            React.createElement('input', {
              type: 'password',
              value: apiKeys.openAI,
              onChange: (e) => setApiKeys({...apiKeys, openAI: e.target.value}),
              placeholder: 'OpenAI API 키',
              className: "w-full border rounded-lg p-3"
            })
          )
        ),
        React.createElement('button', {
          onClick: handleSaveKeys,
          className: "w-full mt-6 bg-purple-600 text-white py-3 rounded-lg hover:bg-purple-700"
        }, 'API 키 저장하고 시작하기')
      ),
      
      step === 1 && React.createElement('div', { className: "bg-white rounded-lg shadow-lg p-8" },
        React.createElement('h2', { className: "text-2xl font-bold mb-4" }, '📹 영상 업로드'),
        React.createElement('div', { className: "border-2 border-dashed border-gray-300 rounded-lg p-12 text-center" },
          React.createElement('input', {
            type: 'file',
            accept: 'video/*',
            onChange: handleFileChange,
            className: "hidden",
            id: 'video-upload'
          }),
          React.createElement('label', { htmlFor: 'video-upload', className: "cursor-pointer" },
            React.createElement('div', { className: "text-6xl mb-4" }, '📁'),
            React.createElement('p', { className: "text-lg font-medium mb-2" },
              videoFile ? `✅ ${videoFile.name}` : '클릭해서 영상 선택'
            )
          )
        ),
        videoFile && React.createElement('button', {
          onClick: handleUpload,
          disabled: uploading,
          className: "w-full mt-6 bg-purple-600 text-white py-3 rounded-lg hover:bg-purple-700 disabled:bg-gray-400"
        }, uploading ? '업로드 중...' : '업로드 시작')
      )
    )
  );
}

ReactDOM.render(React.createElement(App), document.getElementById('root'));
