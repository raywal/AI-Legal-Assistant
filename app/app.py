from flask import Flask, request, render_template
from models.legal_document_processor import LegalDocumentProcessor
from utils.data_preprocessor import DataPreprocessor

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["document"]
        if file:
            document_text = file.read().decode("utf-8")
            preprocessed_text = DataPreprocessor.clean_text(document_text)
            processor = LegalDocumentProcessor()
            clauses = processor.extract_clauses(preprocessed_text)
            return render_template("results.html", clauses=clauses)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
