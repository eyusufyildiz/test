import streamlit as st

def main():
    st.sidebar.title('Navigation')

    # Create links to different pages
    home_page = st.page_link("Home", "Home")
    about_page = st.page_link("About", "About")
    contact_page = st.page_link("Contact", "Contact")

    if st.session_state.navigation == "Home":
        st.title("Home")
        st.write("Welcome to the Home page.")

    elif st.session_state.navigation == "About":
        st.title("About")
        st.write("This is the About page. Here you can find information about us.")

    elif st.session_state.navigation == "Contact":
        st.title("Contact")
        st.write("Contact us via email or phone for further assistance.")
        home_page

if __name__ == "__main__":
    main()
    
