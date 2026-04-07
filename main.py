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

print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)

