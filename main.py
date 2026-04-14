
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

resume_text = read_file("resume.txt")
job_description = read_file("job_description.txt")

matched, missing, score = analyze_resume(resume_text, job_description, skill_list)
print_results(matched, missing, score)






