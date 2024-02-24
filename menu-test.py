import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.title("Vertical Navigation Menu")

    # Define options for the vertical menu
    options = ["Home", "About", "Contact"]

    # Display vertical navigation menu
    choice = option_menu("Navigation", options, orientation="vertical")

    # Display content based on the selected option
    if choice == "Home":
        st.header("Home")
        st.write("Welcome to the Home page.")

    elif choice == "About":
        st.header("About")
        st.write("This is the About page. Here you can find information about us.")

    elif choice == "Contact":
        st.header("Contact")
        st.write("Contact us via email or phone for further assistance.")

    
main()
