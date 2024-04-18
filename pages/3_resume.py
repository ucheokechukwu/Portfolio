import streamlit as st
import base64

st.set_page_config(page_title="Resume", page_icon="📝")

st.title("📝 Resume")

with open("backend/data/resume.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="1200mm" height="1000mm"               type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    #    <div style="display: flex; justify-content: center;"></div>
    
contact_info = st.secrets['contact_info']
with st.sidebar:
    st.title("Contact Me")
    st.markdown(contact_info, unsafe_allow_html=True)