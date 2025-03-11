import streamlit as st
from streamlit_option_menu import option_menu


EXAMPLE_NO = 1

def streamlit_menu():
    # ใช้ sidebar menu เท่านั้น
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Machine Learning", "Neural Network", "Demo Machine Learning", "Demo Neural Network"],  # เพิ่มหน้า About
                # icons=["house", "book", "envelope", "info-circle"],  # เพิ่มไอคอน
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

selected = streamlit_menu()

if selected == "Machine Learning":
    st.title("Welcome to the Machine Learning Page")
    st.write("This is the main landing page of our app.")
if selected == "Neural Network":
    st.title("Welcome to the Neural Network Page")
if selected == "Demo Machine Learning":
    st.title("Demo Machine Learning")
if selected == "Demo Neural Network":  
    st.title("Demo Neural Network")





















