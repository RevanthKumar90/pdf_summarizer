import streamlit as st
import base64
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text

st.set_page_config(page_title="PDF Summarizer", layout="wide")

# 💡 Stylish Header 
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

logo_base64 = get_base64_image("assets/logo.png")

header_html = """
<div style="display:flex; justify-content: space-between; align-items:center; 
background-color: black; padding: 5px 20px; border-radius: 40px; margin-bottom: 20px;">
<div style="display:flex; align-items:center;">
"""

if logo_base64:
    header_html += f'<img src="data:image/png;base64,{logo_base64}" width="60" style="margin-right:20px;" />'

header_html += """
<h2 style="color:white; margin: 0;">PDF Summarizer</h2>
</div>
<span style="color:white; font-size:12px;">Using T5-small Model</span>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

# 📤 File Upload Section
uploaded_file = st.file_uploader("⬇️ Upload a PDF File", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text_from_pdf(uploaded_file)
        st.session_state["extracted_text"] = extracted_text

    st.success("✅ Text extracted!")

    col1, col2 = st.columns(2)

    # 📜 Extracted Text block
    with col1:
        st.subheader("📜 Extracted Text")
        st.text_area(
            "Extracted Content",
            st.session_state.get("extracted_text", ""),
            height=300
        )

    # 📝 Summary block
    with col2:
        if st.button("✍️ Generate Summary"):
            with st.spinner("⏳ Summarizing..."):
                summary = summarize_text(st.session_state["extracted_text"])

                formatted_summary = ""
                for line in summary.split(". "):
                    if line.strip():
                        formatted_summary += f"- {line.strip()}\n"

                st.session_state["summary"] = formatted_summary

            st.success("✅ Summary ready!")

        if st.session_state.get("summary"):
            st.subheader("📝 Summary")
            st.text_area(
                "Summary Output",
                st.session_state["summary"],
                height=300
            )

            st.download_button(
                label="💾 Download Summary",
                data=st.session_state["summary"],
                file_name="summary.txt",
                mime="text/plain"
            )
