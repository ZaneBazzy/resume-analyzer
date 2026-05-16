# AI Resume Analyzer + Job Match Tool

A full-stack AI-powered web application that analyzes resumes against job descriptions using Python, Flask, and the Google Gemini API.

The application allows users to upload resumes and job descriptions in PDF or TXT format, then generates:

* Match scores
* Matched skills
* Missing skills
* Resume feedback
* Suggested project improvements
* AI-generated summaries

The project was built to simulate how applicant tracking systems (ATS) and AI-assisted recruiting tools compare resumes to job postings.

---

# Live Demo

https://resume-analyzer-n3yx.onrender.com

---

# Features

* Upload PDF or TXT resumes
* Upload PDF or TXT job descriptions
* AI-powered resume analysis using Google Gemini API
* Match score visualization
* Matched and missing skill detection
* Resume improvement feedback
* Suggested project recommendations
* Responsive Bootstrap user interface
* Deployed live using Render

---

# Tech Stack

## Programming Languages

* Python
* HTML/CSS

## Tools & Frameworks

* Flask
* Bootstrap
* Git
* GitHub
* Render
* Google Gemini API

## Libraries

* pypdf
* python-dotenv

---

# Project Structure

```text
resume-analyzer/
│
├── main.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   └── style.css
│
├── uploads/
│
└── .env
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/ZaneBazzy/resume-analyzer.git
cd resume-analyzer
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create a .env file

Create a file named:

```text
.env
```

Add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

---

# Running the Application

Run the Flask app:

```bash
python main.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

# Example Workflow

1. Upload a resume
2. Upload a job description
3. Click "Analyze Match"
4. View:

   * Match score
   * Matched skills
   * Missing skills
   * Resume feedback
   * Suggested projects
   * AI-generated summary

---

# Future Improvements

* Resume bullet point rewriting
* Drag-and-drop uploads
* Downloadable PDF reports
* User authentication
* Database storage
* More advanced NLP analysis
* ATS optimization suggestions

---

# What I Learned

Through this project I learned:

* Full-stack web application development
* Flask backend development
* File upload handling
* PDF text extraction
* API integration
* Environment variable security
* Frontend styling with Bootstrap
* Git/GitHub version control
* Cloud deployment with Render
* AI-assisted application workflows

---

# Screenshots

<img width="1049" height="582" alt="image" src="https://github.com/user-attachments/assets/124473a6-3114-4f75-9a9e-c98b5ca5dd07" />

<img width="936" height="528" alt="image" src="https://github.com/user-attachments/assets/339e98e0-9c33-4ae5-b2b6-469f928fddcf" />

<img width="1108" height="947" alt="image" src="https://github.com/user-attachments/assets/4916eac9-204a-4638-945c-411e907db4c2" />

---

# Author

Zane Bazzy
