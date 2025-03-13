import streamlit as st

# App Title and Description
st.title("Simple Streamlit App")
st.markdown("This is a simple app that takes user input and displays it back to the user.")

# User Input
user_input = st.text_input("Enter some text:", placeholder="Type something here...")

# Button to Show Text
if st.button("Show Text"):
    if user_input:
        st.success(f"You Entered: **{user_input}**")
    else:
        st.warning("Please enter some text before clicking 'Show Text'.")
