import streamlit as st
from st_pages import add_page_title, add_indentation
import utils
from PIL import Image

# Adds company logo at the top of sidebar
utils.add_company_logo()

# add_page_title()
add_indentation()

def admin_page():
    st.title("Admin Page")

    st.write("")
    st.write("")
    st.write("")

    with st.container():
        with st.expander(" Send Reminder for Appointment"):
            exp1=Image.open("images/exp1_2.png")
            st.image(exp1,use_column_width=True)

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        with st.expander(" Edit the notification message"):
            st.write("")
            # exp1=Image.open("images\exp1.png")
            # st.image(exp1,use_column_width=True)

# authenticator = st.session_state['authenticator']
# with st.sidebar:
#     authenticator.logout("Logout", "sidebar")