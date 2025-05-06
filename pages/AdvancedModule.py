import streamlit as st

def AdvancedModule():
    Basic_Module_Text = "\
    Welcome!\n\
    Ex00: Odd and Even\n\
    Loop across all numbers from -111 to 111 all included.\n\
    Fill the arrays 'even' and 'odd' fittingly.\n\
    Bonus: Repeat, this time, fill the arrays without any condition checking.\n\
    Ex01: Complete Numbers\n\
    Google what 'complete numbers' are, then fill an array with all those you can find from 2 to 500k.\n\
    Optimize your code for speed\n\
    Ex02: Palindromes\n\
    Google what palindromes are, then write the code that checks if the user_input (in a loop) is one.\n\
    Now write a function that transforms the user_input into a palindrome if it isnt one yet.\n\
    Ex03: Fermats Last Theorem\n\
    Research the wild story of Fermats Last Theorem.\n\
    now write a program that loops a quiz on 10 different facts from that story. Use formatted printing, arrays.\n\
    Ex04: Slicing\n\
    Create the array 'slice_me', having all values from -50 incl. to 50 incl.\n\
    Create the array 'halfes', and fill it with 2 arrays, each containing one half of 'slice_me'\n\
    Create the array 'thirds', and fill it with 3 arrays, each containing one third of 'slice_me'\n\
    Create the array 'quarters', and fill it with 4 arrays, each containing one quarter of 'slice_me'\n\
    Bonus:\n\
    Gather the logic for slicing the array into arrays that each only contain 2 elements.n\
    "
    with st.expander("Advanced Module"):
        st.write("Learn the Basic for building more later.")
        st.download_button(
            label="Download Subject",
            data=Basic_Module_Text,
            file_name="Advanced_Module.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    AdvancedModule()