import streamlit as st
def sidebar():
    with st.sidebar:
        st.title("About Me")
        st.markdown(
        "Uche J is an AI/ML Data Scientist with a knack for solving problems and passionate about using AI to drive solutions. Currently freelancing as an AI Trainer, and open to exciting new opportunities.")
    
        st.markdown("In this app, you can:")
    
        st.markdown("""
        - Ask my AI Assistant J-Bot about me.
        - Check out the projects in my portfolio.
        - Browse through my resume. """)
     

        contact_info = st.secrets['contact_info']
        st.title("Contact Me")
        st.markdown("""Have questions that J-Bot can't answer? Or just want to get in touch? Then fill out the contact form and I'll get back to you ASAP.""") 
        st.markdown(contact_info, unsafe_allow_html=True)