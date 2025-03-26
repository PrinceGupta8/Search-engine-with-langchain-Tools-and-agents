from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchResults
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_community.utilities import SerpAPIWrapper

#search=SerpAPIWrapper(serpapi_api_key='')


api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=400)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=400)
arx = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search=DuckDuckGoSearchResults(name='Search')

st.title('Search Engine')
api_key=st.sidebar.text_input('Enter your groq api key',type='password')

if 'messages' not in st.session_state:
    st.session_state['messages']=[
        {'role':'assistant','content':'Hi , I am a assistant who can search the web. How can I help yoy?'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt:=st.chat_input(placeholder='What is machine Machine Learning?'):
    st.session_state.messages.append({'role':'user','content':prompt})
    st.chat_message('user').write(prompt)
    llm=ChatGroq(model_name='mixtral-8x7b-32768',api_key=api_key,streaming=False)
    tools=[search,arx,wiki]
    search_agent=initialize_agent(tools=tools,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)
    with st.chat_message('assistant'):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant','content':response})
        st.write(response)
