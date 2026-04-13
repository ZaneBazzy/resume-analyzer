
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

    if len(matched_skills) + len(missing_skills) > 0:
        match_score = (len(matched_skills) / (len(matched_skills) + len(missing_skills))) * 100
    else:
        match_score = 0


    return matched_skills, missing_skills, match_score

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

resume_text = """
I am a computer science student with experience in Python, Java, SQL, and Git.
I have also worked with HTML and CSS on small class projects.
"""

job_description = """
We are looking for a candidate with experience in Python, SQL, AWS, machine learning,
Git, and data analysis.
"""

matched, missing, score = analyze_resume(resume_text, job_description, skill_list)


print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Match Score:", round(score, 2), "%")

