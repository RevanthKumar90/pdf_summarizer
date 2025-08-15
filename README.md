# 📄 PDF Summarizer

PDF Summarizer is a web app built using Streamlit that lets you quickly extract text from PDF files and generate concise summaries using HuggingFace transformer models.

## 🚀 Live Demo

Try out the project online:  
[PDF Summarizer App](https://pdfsummarizer-rhmvsqpamwwp8e49jesch9.streamlit.app/)

---

## 💡 Features

- **Extract text** from PDF files (supports direct text-based PDFs).
- **Generate summaries** for the extracted content using state-of-the-art NLP models.
- **Download summary** as a text file.
- **User-friendly interface** – drag and drop PDFs, instant results.

---

## ⚠️ Limitations

- *Scanned/image-based PDFs*: Currently, OCR (Optical Character Recognition) is disabled. If the PDF doesn’t have a text layer, extraction won’t work.
- *Copy to Clipboard*: This feature works only on local machines. On web deployment, backend cannot access user clipboard due to browser security restrictions.

---

## 📱 How To Use

1. **Open the app** in your browser ([Live link above](https://pdfsummarizer-rhmvsqpamwwp8e49jesch9.streamlit.app/)).
2. **Upload a PDF file** (text-based preferred).
3. **See extracted text** instantly.
4. **Click “Generate Summary”** to get a short summary.
5. **Download** summary as a `.txt` file.
6. **Copy summary** manually from the text area if needed.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **PyMuPDF, pdf2image, pytesseract** (PDF extraction)
- **HuggingFace Transformers**
- **Torch**

---

## 📦 Installation (for local development)

git clone https://github.com/revanthkumar90/pdf_summarizer.git
cd pdf_summarizer

python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

pip install --upgrade pip
pip install -r requirements.txt

streamlit run app.py  
undefined

## 💡 Usage Tips

- Use text-based PDFs for best results.
- For scanned/image PDFs, OCR is currently disabled but may be added in future versions.
- For better summaries, keep PDFs concise if possible.
- If summary generation takes longer, please be patient as it uses transformer models.

  
## 🤝 Contributing

Contributions are welcome! If you'd like to improve the app or add features:

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and test thoroughly.
4. Submit a pull request with a detailed description.

Please follow coding guidelines and maintain code clarity.

## 🖼️ Screenshots

Here are some screens of the app in action:

### App Home & PDF Upload

![PDF Summarizer - Home](<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/00aaf034-67e8-436e-84e2-fe118f3e8f76" />)

### Extracted Text Example

![PDF Extraction Example](<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/4cd793c9-5fb1-4dd4-94e4-e0695b44d683" />)

### Summary Generation Example

![PDF Summary Example](<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/2422dbf0-27c0-4a82-b084-04425f9482eb" />)



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

