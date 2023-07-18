import streamlit as st
from st_pages import add_page_title, add_indentation
import utils
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# Adds company logo at the top of sidebar
utils.add_company_logo()
 
# add_page_title()
add_indentation()

authenticator = st.session_state['authenticator']
with st.sidebar:
    authenticator.logout("Logout", "sidebar")
    
# redirect to login page
if st.session_state['logout'] == True:
    switch_page('Admin')

def doctor_page():
    st.title("Doctor Page")

    st.write("")
    st.write("")
    st.write("")

    static_doctor_content=Image.open("images/Doctor_page_static content.png")
    st.image(static_doctor_content,use_column_width=True)

doctor_page()