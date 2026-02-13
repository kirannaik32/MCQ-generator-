from flask import Flask, render_template, request
import PyPDF2
from mcq import generate_mcqs

app = Flask(__name__)

def extract_text(file):
    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    else:
        return file.read().decode("utf-8")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        count = int(request.form["count"])
        text = extract_text(file)
        mcqs = generate_mcqs(text, count)
        return render_template("result.html", mcqs=mcqs)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)