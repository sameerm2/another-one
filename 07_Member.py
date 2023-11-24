import streamlit as st
from st_pages import add_page_title, add_indentation
from member_v2 import member_page
import utils
from streamlit_extras.switch_page_button import switch_page

# Adds company logo at the top of sidebar
utils.add_company_logo()
 
add_indentation()

#st.markdown("<h1 style='text-align: center; color: black;'>Generative-AI Assisted Medical Records Extraction</h1>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; color: black;'> AI Assisted Document Extraction</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'> GenAI Led Document Information Extraction</h1>", unsafe_allow_html=True)
authenticator = st.session_state['authenticator']
with st.sidebar:
    authenticator.logout("Logout", "sidebar")
    
if st.session_state['logout'] == True:
    switch_page('Admin')
    
member_page()

