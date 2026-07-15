import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject Code", placeholder = "CS101")
    sub_name = st.text_input("Subject Name", placeholder = "Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder = "G2")

    st.button("Create Subject ")