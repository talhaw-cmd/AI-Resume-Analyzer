import React, { useEffect, useState } from 'react'
import './App.css'
const API_URL = import.meta.env.VITE_API_URL;

const App = () => {
  const [msg, setmsg] = useState("")
  const [file, setfile] = useState(null)
  const [skills, setskills] = useState([])
  const [miss_skills, setmiss_skills] = useState([])
  const [suggestions, setsuggestions] = useState([])
  const [score, setscore] = useState("")
  const [strengths, setstrengths] = useState([])
  const [weaknesses, setweaknesses] = useState([])
  const [loading, setloading] = useState(false)

  useEffect(() => {
  console.log("API URL:", API_URL);

  }, [])
  


  let uploaded = async () => {
    if (!file) {
      alert("Please select a PDF");
      return;
    }
    const formData = new FormData();
    formData.append("file", file);

    setloading(true)

    try {
      let res = await fetch(API_URL, {
        method: "POST",
        body: formData
      })
      let data = await res.json()
      setmsg(data.message)
      setskills(data.skills)
      setscore(data.overall_score)
      setmiss_skills(data.missing_skills)
      setsuggestions(data.ai_suggestions)
      setweaknesses(data.weaknesses)
      setstrengths(data.strengths)
    } catch (error) {
      console.error(error)
    }

    setloading(false)
  }

  return (
    <div className="page">
      {/* Background Decorative Blobs */}
      <div className="blob blob-1"></div>
      <div className="blob blob-2"></div>

      {/* Header */}
      <div className="header">
        <span className="badge">AI Powered</span>
        <h1 className="header-title">Resume <span>Analyzer</span></h1>
        <p className="header-sub">Upload your resume and get ultra-fast instant AI optimization feedback.</p>
      </div>

      {/* Upload Card */}
      <div className="card upload-card">
        <h2 className="card-title">Upload Your Resume</h2>
        <p className="card-desc">Drag and drop or browse your PDF file</p>

        <div className={`upload-area ${file ? 'has-file' : ''}`}>
          <input
            type="file"
            accept=".pdf"
            id="file-upload"
            className="file-input"
            onChange={(e) => setfile(e.target.files[0])}
          />
          <label htmlFor="file-upload" className="file-label">
            <span className="upload-icon">📄</span>
            <span className="file-name-text">
              {file ? file.name : "Choose a PDF file..."}
            </span>
          </label>
        </div>

        <button
          className={`btn ${loading ? "btn-loading" : ""}`}
          onClick={uploaded}
          disabled={loading}
        >
          {loading ? (
            <>
              <span className="spinner"></span> Analyzing Resume...
            </>
          ) : "Analyze Resume"}
        </button>
          <br />
        {msg && <p className="msg-box">{msg}</p>}
      </div>

      {/* Score Card */}
      {score && (
        <div className="card score-card">
          <p className="score-label">Overall Match Rating</p>
          <div className="score-circle">
            <h1 className="score-value">{score}</h1>
            <span className="score-max">/ 100</span>
          </div>
        </div>
      )}

      {/* Results Grid */}
      {(strengths.length > 0 || weaknesses.length > 0 || miss_skills.length > 0 || suggestions.length > 0) && (
        <div className="results-grid">

          {strengths.length > 0 && (
            <div className="card result-card strengths-card">
              <h2 className="card-title green">✨ Strengths</h2>
              <ul className="result-list">
                {strengths.map((e, index) => (
                  <li key={index} className="result-item">{e}</li>
                ))}
              </ul>
            </div>
          )}

          {weaknesses.length > 0 && (
            <div className="card result-card weaknesses-card">
              <h2 className="card-title red">🎯 Areas of Improvement</h2>
              <ul className="result-list">
                {weaknesses.map((e, index) => (
                  <li key={index} className="result-item">{e}</li>
                ))}
              </ul>
            </div>
          )}

          {miss_skills.length > 0 && (
            <div className="card result-card missing-card">
              <h2 className="card-title orange">💡 Missing Key Skills</h2>
              <ul className="result-list">
                {miss_skills.map((e, index) => (
                  <li key={index} className="result-item">{e}</li>
                ))}
              </ul>
            </div>
          )}

          {suggestions.length > 0 && (
            <div className="card result-card suggestions-card">
              <h2 className="card-title blue">🚀 AI Next Steps</h2>
              <ul className="result-list">
                {suggestions.map((e, index) => (
                  <li key={index} className="result-item">{e}</li>
                ))}
              </ul>
            </div>
          )}

        </div>
      )}
    </div>
  )
}

export default App