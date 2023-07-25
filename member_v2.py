import streamlit as st
from pathlib import Path
import os, random
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
import openai
from langchain.embeddings import HuggingFaceEmbeddings, OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
# from speech_to_text import * #edited by Sudip
import speech_recognition as sr
#from mic_access_streamlit import *
import tempfile
from st_custom_components import st_audiorec
from audio_recorder_streamlit import audio_recorder
from pydub import AudioSegment as am
from admin import admin_page
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

r = sr.Recognizer()

# extract text from pdf
@st.cache_data()
def extract_text(pdf_path):
    # extracted_text = text = high_level.extract_text(pdf_path, "")
    doc_reader = PdfReader(pdf_path)
    raw_text = ""
    for page in doc_reader.pages:
        raw_text += page.extract_text()
    # raw_text = raw_text.replace(' ', '')
    # raw_text = raw_text.replace('\n', ' ')
    return raw_text


# extract text from multiple pdf files
@st.cache_data()
def extract_text_multiple(pdfs_folder):
    # extracted_text = text = high_level.extract_text(pdf_path, "")
    raw_text = ""
    for pdf_file in pdfs_folder:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(pdf_file.read())
           
        doc_reader = PdfReader(temp_path)
        for page in doc_reader.pages:
            raw_text += page.extract_text()
        # raw_text = raw_text.replace(' ', '')
        # raw_text = raw_text.replace('\n', ' ')
    return raw_text

# get a response
def get_answer(query, pdf_text):
    answer = f'query:\n{query}\n\nextracted text:\n{pdf_text}'
    return answer

@st.cache_resource()
def get_embeddings():
    return HuggingFaceEmbeddings()
    # return OpenAIEmbeddings()

# Returns Question Answer object
@st.cache_resource()
def get_qa_chain():
    return load_qa_chain(OpenAI(), chain_type="stuff")

# Returns Chunks
@st.cache_resource()
def get_chunk_lst(pdf_text):
    splitter = CharacterTextSplitter(
                separator = ".",
                chunk_size = 200,
                chunk_overlap = 100,
                length_function = len
            )
    chunk_lst = splitter.create_documents([pdf_text])
    return chunk_lst

# Translate Text
def convert_to_regional(input_text,language):
    llm = OpenAI(temperature=0)
    prompt = PromptTemplate(
        input_variables=["text", "language"],
        template="Translate the {text} in {language}",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({
        'text': input_text,
        'language': language
        })
    print(result)
    return result

def member_page(member_name=None):
    #st.title("GenAI-Assisted Medical Records Extraction")
    # st.markdown("<h1 style='text-align: center; color: black;'>Generative-AI Assisted Medical Records Extraction</h1>", unsafe_allow_html=True)
    # file selection dropdown menu
    # st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
    # selected_file = st.selectbox("Select a PDF [[All Reports](https://drive.google.com/drive/folders/1BocjhYw5_XB6113__FNtL4eTt1mSpE3z)]",
    #                              pdf_files)
    pdfs_folder = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
    
    ### OpenAI API Key
    api = st.secrets["openai_api_key"]
    # load_dotenv()
    # api = os.getenv("openai_api_key")
    os.environ["OPENAI_API_KEY"] = api

    question=""
    
    # input question
    ask_text = st.text_input("Ask a Question")
    col1, col3,  col2 = st.columns([2, 3, 2])
    with col1:
        ask_button = st.button("Ask", use_container_width=1)
    with col2:
        # speak_button = st.button("Speak", use_container_width=1)
        # audio_bytes = audio_recorder(text="", icon_size="2x") -> small button
        audio_bytes = audio_recorder(text = "Click to record", icon_size="2x", key="audio_button")
        
    st.markdown(
        """
        <style>
            .body {
                <button type="button" class="btn btn-primary">Primary</button>
            }
        </style>
        """,
            unsafe_allow_html=True,
    )
    
    # Speech to Text
    # st.write("Click the 'Start' button and speak into your microphone.")
    if audio_bytes:
        text=""
        filename = str(random.randint(1,199))+".wav"
        with open(filename, mode='bx') as f:
            f.write(audio_bytes)
            sound = am.from_file(filename, format='wav', frame_rate=44100)
            sound = sound.set_frame_rate(16000)
            sound.export(filename, format='wav')
            harvard = sr.AudioFile(filename)
            with harvard as source:
                audio = r.record(source)
            try:
                # text_en = r.recognize_google(audio, language="en-US", with_confidence=True)
                text_te = r.recognize_google(audio, language="te-IN")
                # print(text_en, text_te)
                # if text_en[1]>=text_te[1]:
                #     text = text_en[0]
                # else:
                #     text = text_te[0]
                text = text_te
                    
            except Exception as e:
                st.write("Try Again")
        
        os.remove(filename)
        # question_speech = speechTotext()  #edited by sudip
        question = text
    
    # Text input
    if ask_button:
        question = ask_text
    
    # If PDF files are selected
    if pdfs_folder:
        pdf_text = extract_text_multiple(pdfs_folder)
        
        ### GenerativeAI
        chunk_lst = get_chunk_lst(pdf_text)
        embeddings = get_embeddings()
        doc_search = FAISS.from_documents(chunk_lst, embeddings)
        chain = get_qa_chain()
        
        if question!="":
            st.write("You Asked:", question)
            st.write("please wait...")
            
            query = question
            docs = doc_search.similarity_search(query)
            
            try:
                op = chain.run(input_documents=docs, question=query)
                if (op==" I don't know." or op==" I'm sorry, I don't understand the question." or op=="I don't know." or op==" Sorry,i don't know"):
                    st.write("Apologies! The information you have requested is not available at this point")
                else:
                    regional_text = convert_to_regional(input_text=op,language='telugu')
                    st.write(regional_text)
                    st.write(op)
                    
            except Exception as e:
                st.write("Apologies! The information you have requested is not available at this point")
            
            audio_bytes = False
            ask_button = False
            question=""
        
    # Else use vector db with member information
    # else:
    #     if member_name is not None:
    #         embeddings = get_embeddings()
    #         persist_directory = os.path.join("chroma_db", member_name)
            
    #         vectordb = Chroma(persist_directory=persist_directory,
    #                             embedding_function=embeddings)
    #         retriever = vectordb.as_retriever()
    #         query = question
    #         print(query)
            
    #         docs = retriever.get_relevant_documents(query)
    #         print(docs)
            
    #         try:
    #             op = chain.run(input_documents=docs, question=query)
    #             print('2')
    #             if (op==" I don't know." or op==" I'm sorry, I don't understand the question." or op=="I don't know." or op==" Sorry,i don't know"):
    #                 st.write("Apologies! The information you have requested is not available at this point")
    #             else:
    #                 st.write(op)
    #         except Exception as e:
    #             st.write("Apologies! The information you have requested is not available at this point~")
                # audio_bytes = False
                # ask_button = False
                # question=""
    #     else:
    #         st.warning("Please select a PDF.")
                

        
