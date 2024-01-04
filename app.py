"""run: streamlit run app.py"""

import os

import streamlit as st
import pandas as pandas
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.document_loaders import WebBaseLoader
from langchain.agents import create_pandas_dataframe_agent

from dotenv import load_dotenv, find_dotenv

from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
load_dotenv(find_dotenv())


from kexpTools import kexp
kexp = kexp()

openai = OpenAI(temperature=0)

if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False}

def clicked(button):
    st.session_state.clicked[button] = True

st.title("Kexp Music Discovery Interactive App 📻 🤖") ## Emoji source emojipedia.org
st.header("Music Discovery at its finest")
st.subheader("Made By Michael Santoro")

with st.sidebar:
    st.write("""*Hello welcome to the kexp music that matters ai 
            assistant this application should allow you to chat 
            with the data that kexp provides. TO-DO: Add Credits here.*""")
    st.caption("**This is a Caption.**") ## Could use html here to center text

    with st.expander('What is KEXP?'):
        website_loader = WebBaseLoader("https://kexp.org/")
        text = website_loader.load()
        prompt = PromptTemplate.from_template(
    """Describe what KEXP is from this website in a concise and informative way:{text}"""
)
        summary = openai(prompt.format(text=text))
        st.write(summary)

    st.divider()

st.button("Let's Get Started", on_click=clicked,args=[1])
if st.session_state.clicked[1]:
    st.write("""Hello welcome to the kexp music that matters ai 
            assistant this application should allow you to chat 
            with the data that kexp provides.""")
    
    hosts_df = kexp.hosts
    programs_df = kexp.programs

    llm = OpenAI(temperature=0)

    pandas_hosts_agent = create_pandas_dataframe_agent(llm,hosts_df, verbose=True)
    pandas_programs_agent = create_pandas_dataframe_agent(llm, programs_df,verbose=True)

    question = "Describe the data in this data frame."