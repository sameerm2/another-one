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
# from st_custom_components import st_audiorec
from audio_recorder_streamlit import audio_recorder
from pydub import AudioSegment as am
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI

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

def get_qa_chain():
    return load_qa_chain(OpenAI(), chain_type="stuff")

def get_chunk_lst(pdf_text):
    splitter = CharacterTextSplitter(
        separator = " ",
        chunk_size = 300,
        chunk_overlap = 100,
        length_function = len
    )
    chunk_lst = splitter.create_documents([pdf_text])
    return chunk_lst

def get_embedding():
    return OpenAIEmbeddings()

pdfs_folder = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

load_dotenv()
api = os.getenv("openai_api_key")
os.environ["OPENAI_API_KEY"] = api

if st.button('Save Embeddings to ChromaDB'):
    if pdfs_folder:
        pdf_text = extract_text_multiple(pdfs_folder)
        print(pdf_text)
        embeddings = get_embedding()
        chain = get_qa_chain()
        chunk_lst = get_chunk_lst(pdf_text)
        print(chunk_lst)

        persist_directory='./chroma_db/father'
        vectordb = Chroma.from_documents(documents=chunk_lst,
                                    embedding=embeddings,
                                    persist_directory=persist_directory)
        vectordb.persist()
        vectordb = None
        
        # vectordb = Chroma(persist_directory=persist_directory,
        #                             embedding_function=embeddings)
        # retriever = vectordb.as_retriever()
        # query = 'describe the patient'
        # docs = retriever.get_relevant_documents(query)
        # print(docs)
                
        # try:
        #     op = chain.run(input_documents=docs, question=query)
        #     if (op==" I don't know." or op==" I'm sorry, I don't understand the question." or op=="I don't know." or op==" Sorry,i don't know"):
        #         st.write("Apologies! The information you have requested is not available at this point")
        #     else:
        #         st.write(op)
        # except:
        #     print('Does not work')