import streamlit as st
import pymongo
import time

# with st.spinner("Loading..."):
#     time.sleep(2)
c1, c2, c3 = st.columns(3)
conn = pymongo.MongoClient(
    "mongodb+srv://devkumar:@Dev89866@cluster0.kgk4tx3.mongodb.net/?appName=Cluster0"
)
mydb = conn["cv"]
my = mydb["user_info"]
st.header("U s e r P r o f i l e")
str1 = st.session_state["username"]
st.success(f"Welcome:{str1}")

if c1.button("Profile"):
    str1 = st.session_state["username"]

    res = my.find({"username": str1})
    for data in res:
        st.success(f"Username:{data['username']}")
        # st.success(f"Password:{data['username']}")
        st.success(f"Gender:{data['gender']}")
        st.success(f"Address:{data['address']}")
        st.success(f"Dob:{data['dob']}")
        # img1 = data["photo"]
        # st.image(img1, width=100)

if "show_pass" not in st.session_state:
    st.session_state.show_pass = False

if c2.button("Change Password"):
    st.session_state.show_pass = True

if st.session_state.show_pass:

    t1 = st.text_input("Old Password", type="password")
    t2 = st.text_input("New Password", type="password")

    if st.button("Update Password"):

        result = my.update_one(
            {"password": t1},
            {"$set": {"password": t2}}
        )

        if result.modified_count > 0:
            st.success("Password Changed Successfully!")
        else:
            st.error("Wrong Old Password")
if c3.button("Analyse CV"):
    pass
