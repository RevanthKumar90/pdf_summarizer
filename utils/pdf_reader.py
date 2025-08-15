import fitz  # PyMuPDF
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    text = ""
    # Try text-based extraction
    pdf_data = pdf_file.read()
    with fitz.open(stream=pdf_data, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    
    # If no text found, give a message
    if not text.strip():
        text = "Sorry, this PDF does not contain text that can be extracted directly. The OCR feature is currently disabled."
    
    return text