# Simple AI Resume Analyzer

## ✅ What It Does
Takes in two .txt files: resume and job description
- Cleans and tokenizes text
- Shows keyword overlap between resume and job
- Displays top keywords in the resume
- Calculates readability (Flesch Reading Ease)
- Suggests missing job-related keywords

## 📦 Installation & Usage

1. **Install dependencies**
Run the command
`pip install nltk scikit-learn textstat rich`

2. **Set up Resume & Job Description**
Set up the Resume and Job Description for the code to analyze
Example of your_resume.txt:
```
John Doe is a data analyst with experience in Python, SQL, and Tableau. He has worked on data cleaning, visualization, and reporting tasks. John is familiar with Excel and Google Sheets, and has collaborated with cross-functional teams to deliver business insights. He's also comfortable working with APIs and writing automation scripts.
```
Example of job_description.txt:
```
We are seeking a data analyst proficient in Python, SQL, and data visualization tools like Tableau or Power BI. The ideal candidate will have experience with data pipelines, statistical analysis, and working in collaborative environments. Knowledge of APIs, dashboards, and automation is a plus.
```

3. **Run the file**
Run this command in Command Prompt
`python main.py your_resume.txt job_description.txt`

You're done!

## Example & Result
Example of your_resume.txt:
```
John Doe is a data analyst with experience in Python, SQL, and Tableau. He has worked on data cleaning, visualization, and reporting tasks. John is familiar with Excel and Google Sheets, and has collaborated with cross-functional teams to deliver business insights. He's also comfortable working with APIs and writing automation scripts.
```
Example of job_description.txt:
```
We are seeking a data analyst proficient in Python, SQL, and data visualization tools like Tableau or Power BI. The ideal candidate will have experience with data pipelines, statistical analysis, and working in collaborative environments. Knowledge of APIs, dashboards, and automation is a plus.
```

Example of Final Result:
```
--- Resume Analysis ---

Readability Score: 63.20

Top Resume Keywords:
 - data: 3 times
 - python: 1 times
 - sql: 1 times
 - tableau: 1 times
 - analysis: 1 times
 - reporting: 1 times
 - visualization: 1 times
 - teams: 1 times
 - collaboration: 1 times
 - automation: 1 times

Similarity to Job Description (TF-IDF):
 81.45%

Missing Important Keywords from Job Description:
 - pipelines
 - dashboards
 - statistical
 - collaborative
 - power
```

If this gets enough traction, I will implement this into a website using CSS. Do enjoy this code.


