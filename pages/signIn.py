import streamlit as st
import pymongo

st.title("SignIn")
t1 = st.text_input("Username")
t2 = st.text_input("Password")
if st.button("SIGNIN"):
    conn = pymongo.MongoClient(
    "mongodb+srv://devkumar:%40Dev89866@cluster0.kgk4tx3.mongodb.net/?retryWrites=true&w=majority"
)
    mydb = conn["cv"]
    my = mydb["user_info"]
    res = my.find({"username": t1, "password": t2})
    v = 0
    for data in res:
        v = v + 1
        st.session_state["username"] = data["username"]
        st.switch_page("pages/profile.py")

    if v == 0:
        st.success("Invalid Login !!!")
