
def analyze_resume(resume_text, job_description):
    resume_skills = resume_text.lower().split()
    job_skills = job_description.lower().split()

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_score = (len(matched_skills) / len(job_skills)) * 100

    return matched_skills, missing_skills, match_score

resume_text = """
Python
Java
SQL
Git
"""

job_description = """
Python
SQL
AWS
Machine Learning
Git
"""

matched, missing, score = analyze_resume(resume_text, job_description)


print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Match Score:", round(score, 2), "%")

