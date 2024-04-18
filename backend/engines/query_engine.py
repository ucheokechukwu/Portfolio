from llama_index.core.prompts import PromptTemplate
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

import streamlit as st
import dotenv
dotenv.load_dotenv()

text_qa_template = PromptTemplate(st.secrets["prompts"]["text_qa_template_str"])
refine_template = PromptTemplate(st.secrets["prompts"]["refine_template_str"])
# memory = ChatMemoryBuffer.from_defaults(token_limit=500)
documents = SimpleDirectoryReader("backend/data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_chat_engine(
        text_qa_template=text_qa_template,
        refine_template=refine_template,
        query_processing={"token_limit": 512}
    )

def agent_invoke(prompt):
    return query_engine.query(prompt)