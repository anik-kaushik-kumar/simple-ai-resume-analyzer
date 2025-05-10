import sys
import os
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import textstat

nltk.download("punkt")
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words("english"))

def load_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in STOPWORDS]
    return tokens

def get_top_keywords(tokens, n=10):
    return Counter(tokens).most_common(n)

def compute_tfidf_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_text])
    similarity = (tfidf_matrix * tfidf_matrix.T).A[0, 1]
    return similarity

def missing_keywords(resume_tokens, job_tokens, top_n=15):
    job_counts = Counter(job_tokens)
    resume_set = set(resume_tokens)
    most_common = [word for word, _ in job_counts.most_common(top_n)]
    return [word for word in most_common if word not in resume_set]

def analyze_resume(resume_path, job_path):
    resume_text = load_file(resume_path)
    job_text = load_file(job_path)

    resume_tokens = clean_text(resume_text)
    job_tokens = clean_text(job_text)

    output_lines = []

    output_lines.append("--- Resume Analysis ---\n")

    readability = textstat.flesch_reading_ease(resume_text)
    output_lines.append(f"Readability Score: {readability:.2f}\n")

    output_lines.append("Top Resume Keywords:")
    for word, count in get_top_keywords(resume_tokens):
        output_lines.append(f" - {word}: {count} times")

    similarity = compute_tfidf_similarity(resume_text, job_text)
    output_lines.append(f"\nSimilarity to Job Description (TF-IDF): {similarity * 100:.2f}%\n")

    output_lines.append("Missing Important Keywords from Job Description:")
    missing = missing_keywords(resume_tokens, job_tokens)
    if missing:
        for word in missing:
            output_lines.append(f" - {word}")
    else:
        output_lines.append(" ✅ No major keywords missing!")

    # Create results directory
    os.makedirs("results", exist_ok=True)

    # Write output to file
    resume_name = os.path.basename(resume_path).replace(".txt", "")
    output_path = os.path.join("results", f"resume_analysis_{resume_name}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"\n✅ Analysis complete! Results saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python resume_analyzer.py resume.txt job.txt")
        sys.exit(1)

    resume_path = sys.argv[1]
    job_path = sys.argv[2]
    analyze_resume(resume_path, job_path)
