from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import fitz
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    age: int


@app.get("/")
def hello():
    return {"message": "Hello from FastAPI"}


@app.post("/add")
def add(user: User):
    return {
        "message": f"{user.name} {user.age}"
    }


skills_db = [
    "Python",
    "JavaScript",
    "React",
    "MongoDB",
    "HTML",
    "CSS",
    "FastAPI",
    "Git"
]


def extract_text(file_path):
    pdf = fitz.open(file_path)

    

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def find_skills(text):
    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def find_missing_skills(found_skills):
    miss_skills = []

    for skill in skills_db:
        if skill not in found_skills:
            miss_skills.append(skill)

    return miss_skills


def calculate_score(found_skills):
    score = (len(found_skills) / len(skills_db)) * 60
    score = round(score, 2)

    return score


def generate_suggestions(score, found_skills):
    suggestions = []

    if score < 50:
        suggestions.append("Add more technologies.")

    if "Git" not in found_skills:
        suggestions.append("Learn Git and mention it in your resume.")

    if "MongoDB" not in found_skills:
        suggestions.append("Learn MongoDB or another database.")

    return suggestions

def projects_count(text):
    start = text.find("PROJECTS")
    end = text.find("EDUCATION")

    if start == -1 or end == -1:
        return 0

    projects_section = text[start:end]

    lines = projects_section.splitlines()

    count = 0

    technologies = [
        "React",
        "HTML",
        "CSS",
        "JavaScript",
        "Vite",
        "FastAPI",
        "MongoDB",
        "Python",
        "Vercel"
    ]

    for i in range(len(lines) - 1):
        current_line = lines[i].strip()
        next_line = lines[i + 1].strip()

        if not current_line or current_line == "PROJECTS":
            continue

        for tech in technologies:
            if tech.lower() in next_line.lower():
                count += 1
                break

    return count

def project_marks(projects):
    if projects == 0:
        return 0

    elif projects == 1:
        return 10

    elif projects == 2:
        return 15

    else:
        return 20

def education_found(text):
    count =0
    if "EDUCATION" in text:
        count=20
    return count

def total_marks(score, projects, edu):
    total = score + projects + edu

    return round(total, 2)

    # return score+projects+edu
    

def ai_resume_analysis(text):
    try:
        prompt = f"""
        You are an ATS Resume Analyzer.

        Analyze the following resume.

        Return ONLY valid JSON.

        Do not write any explanation.
        Do not use markdown.
        Do not use ```json.
        Return only one JSON object.

        Format:

        {{
            "score": 0,
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "suggestions": []
        }}

        Resume:

        {text}
        """

        response = model.generate_content(prompt)
        data = json.loads(response.text)

        return data
    
    except Exception as e:
        print(e)
        HTTPException(
            status_code=500,
             detail="AI service is currently unavailable. Please try again later."
        )



os.makedirs("uploads", exist_ok=True)


@app.post("/uploads")
async def uploads(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = f"uploads/{file.filename}"
    

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)



    text = extract_text(file_path)

    found_skills = find_skills(text)

    miss_skills = find_missing_skills(found_skills)

    score = calculate_score(found_skills)

    suggestions = generate_suggestions(
        score,
        found_skills
    )

    projects = projects_count(text)
    pr_marks = project_marks(projects)

    edu = education_found(text)

    total = total_marks(score, pr_marks, edu)

    ai_reply = ai_resume_analysis(text)
    missing_skills = ai_reply["missing_skills"]
    missing_skills = ai_reply["missing_skills"]
    
    strengths = ai_reply["strengths"]
    weaknesses = ai_reply["weaknesses"]
    ai_suggestions = ai_reply["suggestions"]
    overall_score = ai_reply["score"]
    print(missing_skills)


    return {
        "message": "PDF processed successfully",
        "text": text,
        "skills": found_skills,
        "score": score,
        "miss_skills": miss_skills,
        "suggestions": suggestions,
        "total": total,
        "ai_reply": ai_reply,
        "missing_skills": missing_skills,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "ai_suggestions": ai_suggestions,
        "overall_score": overall_score

        
    }