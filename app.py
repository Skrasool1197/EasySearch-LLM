import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchResults
from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.utilities import GoogleSerperAPIWrapper
import os
import re


# Initialize API Wrappers for Wikipedia and Arxiv
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

arxiv_api_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxive = ArxivQueryRun(api_wrapper=arxiv_api_wrapper)

# DuckDuckGo for general search
search = DuckDuckGoSearchResults(name='Search')

# Set up Streamlit App
st.set_page_config(page_title='Search Engine', layout='wide', page_icon="🔍")
st.title('🔍 **EasySearch**')
st.caption('**A simple and sophisticated search tool to help you get information fast and efficiently.**')
st.markdown('---')

# Sidebar for API Keys
st.sidebar.title('⚙️Settings')
st.sidebar.subheader('API Keys')
api_key = st.sidebar.text_input('**Enter your Groq API Key:**', placeholder='Groq API Key', type='password')
serper_api_key = st.sidebar.text_input('**Enter your Google Serper API Key:**', placeholder='Google Serper API Key', type='password')

st.sidebar.markdown('---')
st.sidebar.caption("Make sure to enter both API keys to unlock full functionality!")


# Initialize Session State
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {
            'role': 'assistant',
            'content': 'Hey, how can I help you today? Type in your query!'
        }
    ]

# Display Previous Messages
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

# Handle User Input
if prompt := st.chat_input(placeholder='Ask me.....'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)

    # LLM Setup
    # Can use different LLM or models 
    llm = ChatGroq(
        groq_api_key=api_key,
        # model_name="Gemma2-9b-It",
        model_name = 'llama-3.1-70b-versatile',
        temperature=0.7
    )
    tools = [wiki, arxive, search]

    search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)
    with st.spinner('**🤖 Assistant is thinking...**'):
        with st.chat_message('assistant'):
            callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            res = search_agent.run(st.session_state.messages)
            #res = search_agent.run(st.session_state.messages, callbacks=[callback])
            st.session_state.messages.append({'role': 'assistant', 'content': res})
            st.write(res)

        with st.spinner('🔎 **Searching for relevant images...**'):
            # Image search query based on user prompt
            image_search = GoogleSerperAPIWrapper(serper_api_key=serper_api_key, type="images")
            image_results = image_search.results(prompt)
            image_urls = [image['imageUrl'] for image in image_results['images'][:2]]

            # Display the images in the Streamlit app
            #st.write("Images related to your query:")
            st.caption('🖼️**Images related to your query:**')
            cols = st.columns(2)  # Creates four columns for images
            for idx, url in enumerate(image_urls):
                with cols[idx]:
                    st.image(url, use_column_width=True)

# Footer
st.markdown('---')
st.write("**Developed by Rasool Shaikh | Powered by Groq, Wikipedia, Arxiv, DuckDuckGo, and Google Serper**")
