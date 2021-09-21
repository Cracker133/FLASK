from flask import Flask,render_template,request
import streamlit as st

def praxis():
    st.title("Learning streamlit")
    name = st.text_input("Student_name","Type Here")
    num = st.text_input("Roll_no","Type Here")
    result =""
    if st.button("Show_result"):
        st.success(f"The Student name is {name} with number {num}")

if __name__=="__main__":
    praxis()