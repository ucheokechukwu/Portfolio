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
    
with st.sidebar:
    
    # ------contact---------
    
    with st.form("contact_form"):
        st.subheader("📨 Contact Me")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")
    
    
        if submit_button:
            # Prepare the data to be posted
            data = {
                "name": name,
                "email": email,
                "message": message
            }
    
            # Post the data to formsubmit.co API
            response = requests.post(f"https://formsubmit.co/ajax/{info['Email']}", data=data)
    
            # Check if the request was successful
            if response.status_code == 200:
                st.sidebar.success("Form submitted successfully!")
            else:
                st.sidebar.error("Failed to submit form. Please try again.")