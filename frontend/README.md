# AI Resume Analyzer

An AI-powered Resume Analyzer built using React, FastAPI, Python, and Google Gemini AI. The application analyzes PDF resumes, extracts text, identifies technical skills, calculates an ATS-style score, detects missing skills, and generates intelligent improvement suggestions using Google's Gemini API.

---

## Features

- Upload resume in PDF format
- Extract text using PyMuPDF
- Detect technical skills
- Identify missing skills
- Calculate ATS-style resume score
- Count projects in the resume
- Detect Education section
- AI-powered resume analysis using Google Gemini
- Strengths analysis
- Weakness detection
- Missing skills recommendation
- Career improvement suggestions
- PDF validation
- Error handling for invalid files
- REST API architecture
- React + FastAPI integration

---

## Tech Stack

### Frontend

- React.js
- JavaScript
- HTML5
- CSS3
- Fetch API

### Backend

- FastAPI
- Python
- PyMuPDF
- Google Gemini API
- Pydantic
- Python-dotenv

---

## Project Structure

```
AI-Resume-Analyzer/

│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── uploads/
│   ├── app.py
│   ├── .env
│   ├── requirements.txt
│   └── ...
│
└── README.md
```

---

## How It Works

1. User uploads a PDF resume.
2. FastAPI validates the uploaded file.
3. PyMuPDF extracts all text from the PDF.
4. Rule-based analysis performs:
   - Skill Detection
   - Missing Skills Detection
   - Project Counting
   - Education Detection
   - Resume Score Calculation
5. Extracted text is sent to Google Gemini AI.
6. Gemini returns:
   - ATS Score
   - Strengths
   - Weaknesses
   - Missing Skills
   - Personalized Suggestions
7. React displays the complete analysis.

---

## API Endpoints

### GET /

Returns backend status.

### POST /uploads

Uploads a resume and returns:

- Extracted Text
- Skills
- Missing Skills
- Resume Score
- AI Analysis
- Suggestions

---

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Environment Variables

Create a `.env` file inside the backend folder.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Current Features

- PDF Upload
- PDF Validation
- Resume Parsing
- Text Extraction
- Skill Detection
- Missing Skill Detection
- ATS Score Calculation
- Project Counting
- Education Detection
- AI Resume Analysis
- AI Suggestions
- Error Handling

---

## Future Improvements

- Drag & Drop Upload
- Resume Keyword Matching
- Job Description Comparison
- Resume Improvement Generator
- Download AI Report as PDF
- Authentication
- User Dashboard
- Resume History
- Dark Mode
- Multiple Resume Comparison
- Resume Templates
- Cloud Storage

---

## Learning Outcomes

This project helped me learn:

- React Fundamentals
- FastAPI
- REST APIs
- File Upload Handling
- PDF Processing
- JSON Communication
- Python Functions
- API Integration
- Environment Variables
- Error Handling
- AI Integration using Google Gemini
- Full Stack Development
- Client-Server Architecture

---

## Author

Talha Rauf

---

## License

This project is created for learning purposes and portfolio demonstration.