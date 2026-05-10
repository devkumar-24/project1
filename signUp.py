import streamlit as st
import random
import pymongo

st.header("SignUp")
c1,c2=st.columns(2)
name=c1.text_input("User Name")
Password=c1.text_input("Password")
c=c1.selectbox("Course",['BCA','IT','CS','AI & ML'])
g=c1.radio("Gender",['M','F'])
address=c2.text_area("Address")
dob=c2.date_input("DOB")
co=c2.color_picker("Select Color",value="#00f900")
web_cam=c2.camera_input("Take a picture")
count=random.randint(1,100)
str1="img"+str(count)+".png"
st.write(str1)
with open(str1,"wb") as f:
       f.write(web_cam.getvalue())
b1=st.button("SAVE")
def get_data():
       st.success("Following Deatils are save successfully")
       st.write(name)
       st.write(Password)
       st.write(c)
       st.write(g)
       st.write(address)
       st.write(dob)
       st.write(co)
       st.write(str1)
       conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
       mydb=conn["cv"]
       my=mydb["user_info"]
       my.insert_one({"username":name,"password":Password,"course":c,"gender":g,"address":address,"dob":str(dob),"color":co,"photo":str1})
       st.success("You are regisstered !!!")
       
       
       
if b1:
       get_data()