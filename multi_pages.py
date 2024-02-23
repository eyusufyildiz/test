import streamlit as st

# Define page names
PAGE_HOME = "Home"
PAGE_ABOUT = "About"
PAGE_CONTACT = "Contact"

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
    main()
