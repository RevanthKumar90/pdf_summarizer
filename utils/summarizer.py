import streamlit as st
import torch
from transformers import pipeline

# Load summarization model once and cache it
@st.cache_resource(show_spinner=False)
def load_summarizer_model():
    with st.spinner("Please wait... The AI model is loading."):
        # Lightweight version of BART for faster deploy & execution
        return pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            device=0 if torch.cuda.is_available() else -1
        )

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
