import fitz # PyMuPDF
from pdf2image import convert_from_bytes
import pytesseract
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    text = ""
    
    # First: Try text-based extraction
    pdf_data = pdf_file.read()
    with fitz.open(stream=pdf_data, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    
    # If no text found, fall back to OCR
    if not text.strip():
        images = convert_from_bytes(BytesIO(pdf_data))
        for img in images:
            text += pytesseract.image_to_string(img)
    
    return text