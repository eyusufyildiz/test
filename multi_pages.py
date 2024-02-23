import streamlit as st

# Define page names
PAGE_LOGIN = "Login"
PAGE_HOME = "Home"
PAGE_ABOUT = "About"
PAGE_CONTACT = "Contact"

# Create a function to display the login page content
def display_login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # You can add your login logic here
        if username == "admin" and password == "password":
            st.success("Login successful!")
            # Set session state to indicate successful login
            session_state.logged_in = True
        else:
            st.error("Invalid username or password")

# Create a function to display the Home page content
def display_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page")
    # Add more content as needed

# Create a function to display the About page content
def display_about():
    st.title("About Page")
    st.write("Welcome to the About Page")
    # Add more content as needed

# Create a function to display the Contact page content
def display_contact():
    st.title("Contact Page")
    st.write("Welcome to the Contact Page")
    # Add more content as needed

# Main function to run the Streamlit app
def main():
    st.sidebar.title("Navigation Menu")

    # Check if the user is logged in
    if not hasattr(session_state, "logged_in"):
        session_state.logged_in = False

    if not session_state.logged_in:
        display_login()
    else:
        # Create a radio button for page navigation
        page = st.sidebar.radio("Go to", [PAGE_HOME, PAGE_ABOUT, PAGE_CONTACT])

        # Display the selected page content
        if page == PAGE_HOME:
            display_home()
        elif page == PAGE_ABOUT:
            display_about()
        elif page == PAGE_CONTACT:
            display_contact()

if __name__ == "__main__":
    session_state = SessionState()
    main()

