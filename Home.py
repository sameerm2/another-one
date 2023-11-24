import streamlit as st
from pathlib import Path
import pickle
import streamlit_authenticator as stauth
import os
from streamlit_option_menu import option_menu
# from admin2 import admin_page
# from doctor import doctor_page
# from member_v2 import member_page
from PIL import Image
from family import *
from st_pages import Page, show_pages, add_page_title, Section, add_indentation
import utils



# Authentication:
# hide_bar= """
#     <style>

#     </style>
# """
    # [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
    #     visibility:hidden;
    #     width: 0px;
    # }
    # [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
    #     visibility:hidden;
    # }

# get user information
user_info = {}
cred_path = Path(__file__).parent / "./hashed_passwords.pkl"
with cred_path.open("rb") as file:
    user_info = pickle.load(file)
    
credentials = {
    "usernames":{
        user_info["usernames"][0] : {
            "name" : user_info["names"][0],
            "password" : user_info["passwords"][0]
            }         
        }
}


cookie_name = "sample_app"
authenticator = stauth.Authenticate(credentials, cookie_name, "abcd", cookie_expiry_days=30)

st.session_state['authenticator'] = authenticator
st.session_state['cookie_name'] = cookie_name

name, authentication_status, username = authenticator.login("Login", "main")

def logout():
    authenticator.cookie_manager.delete(cookie_name)
    st.session_state['logout'] = True
    st.session_state['name'] = None
    st.session_state['username'] = None
    st.session_state['authentication_status'] = None

    
# set sidebar collapsed before login
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

# hide collapsed control button
# hide_bar = """
#            <style>
#            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
#                 visibility:hidden;
#                 width: 0px;
#             }
#             [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
#                 visibility:hidden;
#             }
#            </style>
               
#            """
           
hide_bar = '''
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
'''
# [data-testid='collapsedControl"] {display: none;}
# set sidebar expanded after login
# if st.session_state['logout']==False:
#     st.session_state.sidebar_state = 'expanded'

if authentication_status == False:
    st.error("Username/password is incorrect")
    st.markdown(hide_bar, unsafe_allow_html=True)
elif authentication_status == None:
    st.warning("Please enter your username and password")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status:
    # Adds company logo at the top of sidebar
    utils.add_company_logo()
    
    # set logout session state to false 
    st.session_state['logout'] = False
    
    from st_pages import Page, Section, add_page_title, show_pages
    show_pages(
        [
            Page("Home.py", "Admin", "⚙️"),
            #Page("02_Doctor.py", "Doctor", icon="🧑‍⚕️"),
            
            #Section(name="Family", icon="👪"),
            #Page("03_Father.py", "Father", icon="🧓"),
            #Page("04_Son.py", icon="👨"),
            #Page("05_Daughter_in_law.py", icon="👩"),
            #Page("06_Grandson.py", icon="👦"),
            
            Page("07_Member.py", in_section=False, icon="📝"),
            # Page("logout.py", in_section=False)
        ]
    )
    # add_page_title()
    add_indentation()
    
    # page contents
    admin_page()
    
    with st.sidebar:
        authenticator.logout("Logout", "sidebar")
    
    
    # print(st.session_state)
else:
    st.session_state.sidebar_state = 'collapsed'
    st.markdown(hide_bar, unsafe_allow_html=True)

# OLD CODE
#================================================================================================================================
    # if selected_page == "Admin":
    #     admin_page()
    # if selected_page == "Doctor":
    #     doctor_page()
    # if selected_page == "Member":
    #     member_page()
    # if selected_page =="Family":
    #     with st.sidebar:

    #         selected_page = option_menu(

    #         menu_title=None,

    #         options = ["Son", "Daughter","Daughter-in-law","Grandson" ],

    #         icons = ["person-circle","person","person","person-circle"]

    # )

    #     if selected_page == "Son":
    #         son()
    #     if selected_page=="Daughter":
    #         daughter()

    #     if selected_page=="Daughter-in-law":
    #         daughter_in_law()
    #     if selected_page =="Grandson":
    #         grandson()
            
    # if selected_page == "Logout":
    #     logout()
    
    
    #=======================================
