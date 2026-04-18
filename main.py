import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def analyze_resume(resume_text, job_description, skill_list):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in skill_list:
        if skill in job_description:
            if skill in resume_text:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

    total_skills_found = len(matched_skills) + len(missing_skills)

    if total_skills_found > 0:
        match_score = (len(matched_skills) / total_skills_found) * 100
    else:
        match_score = 0
   
    return matched_skills, missing_skills, match_score


    
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

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume_file = request.files.get("resume_file")
    job_file = request.files.get("job_file")

    if not resume_file or not job_file:
        return "Please upload both a resume and a job description file."
    
    if resume_file.filename == "" or job_file.filename == "":
        return "Please select valid files for both resume and job description."
    
    if not allowed_file(resume_file.filename) or not allowed_file(job_file.filename):
        return "Only .txt files are allowed for upload."
    
    resume_filename = secure_filename(resume_file.filename)
    job_filename = secure_filename(job_file.filename)

    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_filename)
    job_path = os.path.join(app.config['UPLOAD_FOLDER'], job_filename)

    resume_file.save(resume_path)
    job_file.save(job_path)

    with open(resume_path, 'r', encoding='utf-8') as f:
        resume_text = f.read()

    with open(job_path, 'r', encoding='utf-8') as f:
        job_description = f.read()
    

    matched, missing, score = analyze_resume(resume_text, job_description, skill_list)

    return render_template("results.html", matched=matched, missing=missing, score=round(score, 2))

if __name__ == "__main__":
    app.run(debug=True)
    


