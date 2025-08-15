import streamlit as st
import torch
from transformers import pipeline

# ------------------- MODEL LOADING -------------------
@st.cache_resource(show_spinner=False)
def load_summarizer_model():
    with st.spinner("Loading AI model..."):
        return pipeline(
            "summarization",
            model="t5-small",   # much faster than bart
            tokenizer="t5-small",
            device=0 if torch.cuda.is_available() else -1
        )

summarizer = load_summarizer_model()

# ------------------- SUMMARIZATION FUNCTION -------------------
@st.cache_data(show_spinner=False)
def summarize_text(text: str, max_chunk: int = 3000) -> str:
    with st.spinner("Summarizing..."):
        if len(text) <= max_chunk:
            return summarizer(
                "summarize: " + text,
                max_length=200,
                min_length=50,
                do_sample=False
            )[0]['summary_text']

        # Process chunks one by one
        chunks = [text[i:i + max_chunk] for i in range(0, len(text), max_chunk)]
        summaries = []
        for chunk in chunks:
            result = summarizer(
                "summarize: " + chunk,
                max_length=200,
                min_length=50,
                do_sample=False
            )[0]['summary_text']
            summaries.append(result)

        return " ".join(summaries).strip()
