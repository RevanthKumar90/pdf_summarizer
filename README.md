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

<img width="1920" height="1020" alt="Screenshot 2025-08-15 202646" src="https://github.com/user-attachments/assets/f06e2841-0e53-49a2-b9fc-7004de1f4187" />

### Extracted Text Example

<img width="1920" height="1020" alt="Screenshot 2025-08-15 202826" src="https://github.com/user-attachments/assets/a4a755c6-c11f-47c9-94a0-09cb27bbb96a" />


### Summary Generation Example

<img width="1920" height="1020" alt="Screenshot 2025-08-15 202937" src="https://github.com/user-attachments/assets/ff04bf4c-0494-4b8c-a7f0-6a768f9c2501" />


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

