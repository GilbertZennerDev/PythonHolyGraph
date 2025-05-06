import streamlit as st
from pages.BasicModule import BasicModule
from pages.AdvancedModule import AdvancedModule

st.header("Welcome to the Python Holy Graph!")

newemail = st.text_input("Enter Your Email For Newsletter ")

if st.button("Sign Up For Newsletter"):
    known_emails = open("emails.txt", "r").read()
    #known_emails = known_emails.read()
    print(f"[debug known emails]{known_emails}")
    file = open("emails.txt", "a")
    if newemail not in known_emails:# and len(newemail) > 3 and '@' in newemail:
        file.write(f"{newemail}\n")

#ADD EMAIL SIGNUP For Newsletter
#ADD a textinput so user can enter his email
#APPEND the email to a emails.txt

#research st.textinput
#add button