from pdfminer.high_level import extract_text
import os

def pdf_to_text(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return None

def extract_all_text(input_folder="papers"):
    texts = []
    for file in os.listdir(input_folder):
        if file.endswith(".pdf"):
            path = os.path.join(input_folder, file)
            text = pdf_to_text(path)
            if text:
                texts.append((file, text))
    return texts
