import { useState } from 'react';

function App() {
  const [inputText, setInputText] = useState('');
  const [resultData, setResultData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async () => {
    // Implement a Loading State while waiting for the AI to respond
    setIsLoading(true);
    setResultData(null);

    try {
      // Use fetch to send the user's input to the backend REST API
      const response = await fetch('http://localhost:8000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ log_text: inputText })
      });

      const data = await response.json();
      console.log("DATA FROM BACKEND:", data); // <--- ADD THIS LINE
      setResultData(data);
    } catch (error) {
      setResultData({ error: "Failed to connect to the API." });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: '30px', maxWidth: '700px', margin: 'auto', fontFamily: 'sans-serif' }}>
      <h1>DevOps Log Error Analyzer</h1>
      <textarea 
        rows="8" 
        style={{ width: '100%', marginBottom: '15px', padding: '10px' }}
        placeholder="Paste Docker, AWS, or server log errors here..."
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button 
        onClick={handleSubmit} 
        disabled={isLoading}
        style={{ padding: '12px 24px', cursor: isLoading ? 'not-allowed' : 'pointer' }}
      >
        {isLoading ? 'Analyzing Infrastructure Logs...' : 'Analyze Log'}
      </button>

      {/* Display the parsed JSON data neatly on the UI[cite: 1] */}
      {resultData && (
        <div style={{ marginTop: '20px', padding: '20px', backgroundColor: '#f9f9f9', borderRadius: '8px' }}>
          {resultData.error ? (
            <p style={{ color: 'red', fontWeight: 'bold' }}>{resultData.error}</p>
          ) : (
            <div>
              <p><strong>Error Type:</strong> {resultData.error_type}</p>
              <p><strong>Severity:</strong> <span style={{ color: resultData.severity === 'High' ? 'red' : 'orange'}}>{resultData.severity}</span></p>
              <p><strong>Root Cause:</strong> {resultData.root_cause}</p>
              <p><strong>Fix Commands:</strong></p>
              <ul style={{ listStyleType: 'none', padding: 0 }}>
                {resultData.fix_commands?.map((cmd, idx) => (
                  <li key={idx} style={{ backgroundColor: '#2d2d2d', color: '#fff', padding: '8px', margin: '4px 0', fontFamily: 'monospace' }}>
                    {cmd}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;