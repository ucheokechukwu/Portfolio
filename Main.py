import streamlit as st
import requests 
from backend.engines.query_engine import agent_invoke
from sidebar import sidebar
import time

st.set_page_config(page_title="Home", page_icon="🏡")
sidebar()

_, col , _ = st.columns([0.1  , 1.0, 0.01])
with col:
    st.title("Uche Jacqueline Okechukwu")
st.info("Machine Learning Engineer | Data Scientist")

_stream_data = st.secrets['about_me']

def stream_data():
    for word in _stream_data.split(" "):
        yield word + " "
        time.sleep(0.2)

_, _, col , _, _ = st.columns(5)

with col:
    center_button = st.button("Who is Uche?", key="info")

if center_button:
    # Call the write_stream function here
    st.write_stream(stream_data)    

st.divider()   



# ############ ---- CHATBOT ----- ################
# st.info(
#     "👋 I am J-Bot, Uche's 🤖 assistant."
# )
#
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
#
# for message in st.session_state.messages:
#     with st.chat_message(message['role']):
#         if "output" in message.keys():
#             st.markdown(message['output'])
#         if "explanation" in message.keys():
#             with st.status("How was this generated", state="complete"):
#                 st.info(message["explanation"])
#
# if prompt := st.chat_input("What do you want to know about Uche?"):
#     st.chat_message("user").markdown(prompt)
#     st.session_state.messages.append({"role":"user", "output":prompt})
#
#     # data = {"input": prompt, "chat_history":st.session_state.chat_history}
#     with st.spinner("..."):
#         try:
#             output_text = agent_invoke(prompt).response
#             st.session_state.chat_history += ['Human: '+prompt+'\nAI: '+output_text+'\n']
#         except:
#             output_text = """An error occurred while processing your message.
#             Please try again or rephrase your message."""
#
#
#     st.chat_message("assistant").markdown(output_text)
#
#     st.session_state.messages.append(
#         {"role": "assistant",
#         "output": output_text,
#     }
#     )
