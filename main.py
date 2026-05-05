import os
import json
from dotenv import load_dotenv
from google import genai
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pypdf import PdfReader

app = Flask(__name__)

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', "pdf"}

# Create the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the file exists and is of an allowed type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function to extract skills from text based on a predefined skill list
def extract_skills(text, skill_list):
    text = text.lower()
    found_skills = []

    for skill in skill_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# Function to analyze resume against job description and skill list
def analyze_resume(resume_text, job_description, skill_list):
    resume_skills = extract_skills(resume_text, skill_list)
    job_skills = extract_skills(job_description, skill_list)

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total_skills_found = len(job_skills)

    if total_skills_found > 0:
        match_score = (len(matched_skills) / total_skills_found) * 100
    else:
        match_score = 0

    return matched_skills, missing_skills, match_score


# Function to print results in a user-friendly format   
def print_results(matched, missing, score):
    print("\n=== Resume Analyzer + Job Match Tool ===")
    print(f"Match Score: {round(score, 2)}%")
    print(f"Matched Skills: {len(matched)}")
    print(f"Missing Skills: {len(missing)}")

    print("\nMatched Skills:")
    if matched:
        for skill in matched:
            print(f" - {skill}")
    else:
        print(" None")
    
    print("\nMissing Skills:")
    if missing:
        for skill in missing:
            print(f" - {skill}")
    else:
        print(" None")

    print("\nSuggested Next Steps:")
    if missing:
        print("Consider adding these skills to your resume if you have experience with them:")
        for skill in missing:
            print(f" - {skill}")
    else:
        print("Your resume matches all detected job skills.")

# Function to extract text from uploaded file (txt or pdf)
def extract_text_from_file(file_path):
    extension = file_path.rsplit(".", 1)[1].lower()

    if extension == "txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    if extension == "pdf":
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    return ""

skill_list = [
    "python",
    "java",
    "sql",
    "git",
    "aws",
    "machine learning",
    "data analysis",
    "flask",
    "javascript",
    "html",
    "css"
]

def analyze_with_gemini(resume_text, job_description):
    prompt = f"""
You are an expert career advisor and ATS resume reviewer.

Compare the resume to the job description.

Return ONLY valid JSON in this exact format:
{{
  "match_score": number,
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "resume_feedback": ["feedback1", "feedback2", "feedback3"],
  "suggested_projects": ["project1", "project2"],
  "summary": "short summary"
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    cleaned_response = response.text.strip()

    if cleaned_response.startswith("```json"):
        cleaned_response = cleaned_response.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned_response)

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle file uploads and analysis
@app.route("/analyze", methods=["POST"])
def analyze():
    resume_file = request.files.get("resume_file")
    job_file = request.files.get("job_file")

    if not resume_file or not job_file:
        return "Please upload both files."

    if resume_file.filename == "" or job_file.filename == "":
        return "Please choose both files."

    if not allowed_file(resume_file.filename) or not allowed_file(job_file.filename):
        return "Only .txt and .pdf files are allowed."

    resume_filename = secure_filename(resume_file.filename)
    job_filename = secure_filename(job_file.filename)

    resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_filename)
    job_path = os.path.join(app.config["UPLOAD_FOLDER"], job_filename)

    resume_file.save(resume_path)
    job_file.save(job_path)

    resume_text = extract_text_from_file(resume_path)
    job_description = extract_text_from_file(job_path)

    ai_results = analyze_with_gemini(resume_text, job_description)

    return render_template(
        "results.html",
        matched=ai_results["matched_skills"],
        missing=ai_results["missing_skills"],
        score=ai_results["match_score"],
        feedback=ai_results["resume_feedback"],
        projects=ai_results["suggested_projects"],
        summary=ai_results["summary"]
    )

   

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
    


