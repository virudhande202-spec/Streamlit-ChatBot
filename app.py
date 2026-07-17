
#Module declaration
from langchain_community.llms import Ollama 
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#creating my prompt
prompt = ChatPromptTemplate.from_messages(
    [
         ("system", "you are a helpful assistant. please respond to the question asked"),
        ("user", "Question:{question}")
    ]
)

#streamlit framework
st.title("Virsen Knowledge")
input_text = st.text_input("What question do you have in the mind:")


#Ollama Framework along with gemma2:latest LLM Model
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


# GPT output
if input_text:
   st.write(chain.invoke({"question":input_text}))