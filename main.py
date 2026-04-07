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

print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print("Match Score:", round(match_score, 2), "%")
