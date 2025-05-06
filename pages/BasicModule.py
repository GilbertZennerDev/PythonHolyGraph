import streamlit as st

def BasicModule():
    Basic_Module_Text = "\
    Welcome!\n\
    Ex00: lolaloops\n\
    Write a for loop that loops from 0 included to 10 included. Print the number each time.\n\
    Now write the same loop loop that loops from 0 included to 10 included. Print the number each time.\n\
    Ex01: formatting good\n\
    Define the following string named proof: 'I know how to print formatted'\n\
    Now google how to use the print() command to print the string proof by calling 'proof' and without using any +.\n\
    Ex02: the lord of flies and files\n\
    Google how to create and write the string 'I am the Lord of the flies' to a file named 'lord'. Proof it.\n\
    Google how to load the content of the file into a new string called 'notthelordoftherings'.\n\
    Now print 'notthelordoftherings' using the formatting learned in Ex01.\n\
    Ex03: Line by Line\n\
    Write the code that creates a new file 'linesfile.txt' and save a string into it that contains 7 lines.\n\
    now write a function that opens this file and google how to split the lines, save the result into 'lines'.\n\
    Ex04: Slicing\n\
    Create the array 'slice_me', having all values from -50 incl. to 50 incl.\n\
    Create the array 'halfes', and fill it with 2 arrays, each containing one half of 'slice_me'\n\
    Create the array 'thirds', and fill it with 3 arrays, each containing one third of 'slice_me'\n\
    Create the array 'quarters', and fill it with 4 arrays, each containing one quarter of 'slice_me'\n\
    Bonus:\n\
    Gather the logic for slicing the array into arrays that each only contain 2 elements.\n\
    "
    with st.expander("Basic Module"):
        st.write("Learn the Basic for building more later.")
        st.download_button(
            label="Download Subject",
            data=Basic_Module_Text,
            file_name="Basic_Module.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    BasicModule()