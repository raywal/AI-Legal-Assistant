import re

class DataPreprocessor:
    @staticmethod
    def clean_text(text):
        text = re.sub(r'\n+', ' ', text)  # Remove newlines
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        text = text.strip()
        return text
