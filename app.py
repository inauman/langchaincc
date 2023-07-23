# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

# Set up the OpenAI API
os.environ['OPENAI_API_KEY'] = apikey

# App Framework
st.title("🦜️🔗 LangChain ChatGPT")
prompt = st.text_input("Enter a prompt for the AI to complete:")

# Set up the prompt template
title_template = PromptTemplate(
    input_variables=["topic"],
    template="write me a youtube video title about {topic}"
)
script_template = PromptTemplate(
    input_variables=["title", "wikipedia_research"],
    template="write me a youtube script based on this TITLE: {title} while leveraging this wikipedia research: {wikipedia_research}"
)

# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# Set up llm
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, output_key='title', memory=title_memory, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, output_key='script', memory=script_memory, verbose=True)

# setup SimpleSequentialChain
#sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=["topic"], output_variables=["title", "script"], verbose=True)

wiki = WikipediaAPIWrapper()

# Show the result
if prompt:
    #response = sequential_chain({'topic':prompt})
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)
    #response = {'title':title, 'script':script}
    st.write(title)
    st.write(script)

    with st.expander('Title History'):
        st.info(title_memory.buffer)


    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'):
        st.info(wiki_research)