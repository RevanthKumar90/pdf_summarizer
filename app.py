import streamlit as st
import base64
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text
import pyperclip

st.set_page_config(page_title="PDF Summarizer", layout="wide")

# 💡 Stylish Header
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode()
    return b64_data

# Usage:
logo_base64 = get_base64_image("assets/logo.png")
st.markdown(
    f"""
    <div style="display:flex; justify-content: space-between; align-items:flex-end; background-color: black; padding: 5px 20px; border-radius: 40px; margin-bottom: 20px;">
        <div style="display:flex; align-items:center;">
            <img src="data:image/png;base64,{logo_base64}" width="60" style="margin-right:20px;" />
            <h2 style="color:white; margin: 0;">PDF Summarizer</h2>
        </div>
        <span style="background-color: black; color: white; padding: 4px 8px; border-radius: 8px; font-size: 10px;">
            Used HuggingFace
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# 📤 File Upload Section
uploaded_file = st.file_uploader("⬇️ Upload a PDF File", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text_from_pdf(uploaded_file)
        st.session_state["extracted_text"] = extracted_text
    st.success("✅ Text extracted!")

    # 📑 Extracted Text and Summary Side-by-Side
    col1, col2 = st.columns([2, 2])

    with col1:
        st.subheader("📜 Extracted Text")
        st.text_area("", value=extracted_text[:2000] if extracted_text else "", height=300)

    with col2:
        if st.button("✍️ Generate Summary"):
            with st.spinner("⏳ Summarizing..."):
                summary = summarize_text(extracted_text)
                st.session_state["summary"] = summary
            st.success("✅ Summary ready!")

        if st.session_state.get("summary"):
            st.subheader("📝 Summary")
            st.text_area("", value=st.session_state.get("summary", ""), height=300)
            
            # 💾 Download and Copy buttons side-by-side
            col_dl, col_cp = st.columns([1, 1])
            with col_dl:
                st.download_button(
                    label="💾 Download Summary",
                    data=st.session_state["summary"],
                    file_name="summary.txt",
                    mime="text/plain"
                )
            with col_cp:
                if st.button("Copy to Clipboard"):
                    try:
                        pyperclip.copy(st.session_state["summary"])
                        st.success("✅ Summary copied to clipboard!")
                    except Exception as e:
                        st.error(f"❌ Failed to copy: {e}. Please install 'pyperclip' and try again.")
