import streamlit as st
import base64
from sidebar import sidebar
from streamlit_pdf_viewer import pdf_viewer
import pandas as pd



st.set_page_config(page_title="Resume", page_icon="📝")
sidebar()
st.title("My Resume")




with open("backend/data/resume.pdf", "rb") as f:
    pdf_bytes = f.read()
st.download_button(
        label="Download resume",
        data = pdf_bytes,
        file_name="Uche's Resume.pdf",
        mime="application/pdf"
    )
    
st.divider()

try:
    pdf_viewer("backend/data/resume.pdf")

except:
    with open("backend/data/resume.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="1200mm" height="1000mm"               type="application/pdf"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)

    