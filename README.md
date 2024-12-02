# AI Legal Assistant

The **AI Legal Assistant** is a cutting-edge tool built to revolutionize the legal industry by automating document review using advanced AI models, powered by **Intel® AI PC**. This solution focuses on enhancing legal productivity by extracting critical legal clauses, identifying inconsistencies, and providing actionable insights to users.

This project leverages **Intel®’s AI Stack** including **OpenVINO™, Intel® AI Toolkit**, and other pre-trained models optimized for Intel® hardware to provide faster processing and improved accuracy, all running directly on the client-side (local device).

## Key Features
- **Legal Clause Extraction**: Automatically extract key clauses and provisions from legal documents.
- **Inconsistency Detection**: Identify any inconsistencies or errors within the document.
- **Client-side Processing**: Run all AI models directly on Intel® AI PC for enhanced privacy, faster processing, and reduced reliance on external servers.
- **Actionable Insights**: Provide users with actionable insights to assist in legal document review.

## Technologies Used
- **Intel® AI Toolkit**
- **OpenVINO™**
- **Intel® Neural Compressor**
- **Pre-trained NLP Models from Hugging Face** (Optimized with Intel® technologies)
- **Flask** (for web interface)
- **Python** (Primary programming language)
- **Hugging Face Transformers** (for NLP model)
- **Intel® AI PC Hardware** (CPU, GPU, NPU optimization)

## Getting Started

### Prerequisites
- Python 3.8+
- Intel® AI PC (for hardware optimization) or access to Intel® Tiber AI Cloud
- Required libraries listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/AI-Legal-Assistant.git
    cd AI-Legal-Assistant
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. Visit `http://127.0.0.1:5000/` in your browser to start using the AI Legal Assistant.

## Code Explanation

### models/legal_document_processor.py
This script contains the logic for processing legal documents. It loads the pre-trained NLP model from Hugging Face, processes the document, and extracts legal clauses.
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

class LegalDocumentProcessor:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
    
    def extract_clauses(self, document):
        inputs = self.tokenizer(document, return_tensors="pt")
        outputs = self.model(**inputs)
        # Process the outputs to extract legal clauses
        clauses = self._parse_output(outputs)
        return clauses

    def _parse_output(self, outputs):
        # Process model output and identify legal clauses
        return ["Clause 1", "Clause 2", "Clause 3"]  # Placeholder for actual logic
