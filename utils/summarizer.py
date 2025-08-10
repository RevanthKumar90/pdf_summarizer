import streamlit as st
from transformers import pipeline

# Load summarization model once and cache it
@st.cache_resource(show_spinner=False)
def load_summarizer_model():
    with st.spinner("Please wait... The AI model is loading."):
        return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer_model()

# Summarize text, chunking if too long
@st.cache_data(show_spinner=False)
def summarize_text(text: str, max_chunk: int = 1000) -> str:
    with st.spinner("Summarizing your document... This may take a few minutes."):
        if len(text) <= max_chunk:
            return summarizer(text)[0]['summary_text']

        chunks = [text[i:i + max_chunk] for i in range(0, len(text), max_chunk)]
        summaries = [summarizer(chunk)[0]['summary_text'] for chunk in chunks]

        return " ".join(summaries).strip()
