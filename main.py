import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from PIL import Image
from backend.engines.query_engine import agent_invoke
from backend.utils.helper import *

### SIDEBAR ###
st.set_page_config(page_title="Home", page_icon="🏡")
with st.sidebar:
    st.title("About Me")
    st.markdown(
    "Uche is an AI/ML Data Scientist with a knack for solving problems and passionate about using AI to drive solutions. Currently freelancing as an AI Trainer, and open to exciting opportunities.")
    
    st.markdown("In this app, you can:")
    
    st.markdown("""
    - Ask my AI Assistant J about me.
    - Check out the projects in my portfolio.
    - Browse through my resume. """)
    
    st.markdown("""Have questions that J can't answer? Or just want to get in touch? Then fill out the contact form and I'll get back to you ASAP.""")    



   



############ ---- CHATBOT ----- ################
st.info(
    "👋 I am J, Uche's 🤖 assistant."
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []    
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        if "output" in message.keys():
            st.markdown(message['output'])
        if "explanation" in message.keys():
            with st.status("How was this generated", state="complete"):
                st.info(message["explanation"])
                
if prompt := st.chat_input("What do you want to know about Uche?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user", "output":prompt})

    # data = {"input": prompt, "chat_history":st.session_state.chat_history}
    with st.spinner("..."):
        try:
            output_text = agent_invoke(prompt).response
            st.session_state.chat_history += ['Human: '+prompt+'\nAI: '+output_text+'\n'] 
        except:
            output_text = """An error occurred while processing your message.
            Please try again or rephrase your message."""
            
    
    st.chat_message("assistant").markdown(output_text)
    
    st.session_state.messages.append(
        {"role": "assistant",
        "output": output_text,
    }
    )
