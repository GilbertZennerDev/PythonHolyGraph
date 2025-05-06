import streamlit as st
from pages.BasicModule import BasicModule
from pages.AdvancedModule import AdvancedModule

st.header("Welcome to the Python Holy Graph!")

st.header("Countdown to Release:" + "test")

newemail = st.text_input("Enter Your Email For Newsletter ")

if st.button("Sign Up For Newsletter"):
    known_emails = open("emails.txt", "r").read()
    print(f"[debug known emails]{known_emails}")
    file = open("emails.txt", "a")
    if newemail not in known_emails and len(newemail) > 3 and '@' in newemail:
        file.write(f"{newemail}\n")
        print(f"[debug known emails]{known_emails}")

#ADD A COUNTDOWN WORTH 30 Days.
"""
use st.session to save the value during the loop
"""