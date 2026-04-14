
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

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

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

resume_text = read_file("resume.txt")
job_description = read_file("job_description.txt")

matched, missing, score = analyze_resume(resume_text, job_description, skill_list)

print("=== Resume Analyzer + Job Match Tool ===")
print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Match Score:", round(score, 2), "%")




