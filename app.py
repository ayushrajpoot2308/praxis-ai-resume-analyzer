
from flask import Flask, render_template, request
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resume_text = ""
    skills = ""
    if request.method == "POST":
        file = request.files["resume"]
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                resume_text += page.extract_text()

        vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
        X = vectorizer.fit_transform([resume_text])
        skills = ", ".join(vectorizer.get_feature_names_out())

    return render_template("index.html", resume=resume_text, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
