import streamlit as st
import pymongo

st.header("SignUp")

c1, c2 = st.columns(2)

name = c1.text_input("User Name")
Password = c1.text_input("Password", type="password")

c = c1.selectbox("Course", ['BCA', 'IT', 'CS', 'AI & ML'])

g = c1.radio("Gender", ['M', 'F'])

address = c2.text_area("Address")

dob = c2.date_input("DOB")

co = c2.color_picker("Select Color", value="#00f900")

b1 = st.button("SAVE")


def get_data():

    conn = pymongo.MongoClient(
        "mongodb+srv://devkumar:@Dev89866@cluster0.kgk4tx3.mongodb.net/?retryWrites=true&w=majority"
    )

    mydb = conn["cv"]

    my = mydb["user_info"]

    my.insert_one({
        "username": name,
        "password": Password,
        "course": c,
        "gender": g,
        "address": address,
        "dob": str(dob),
        "color": co
    })

    st.success("You are registered successfully!")


if b1:
    get_data()
