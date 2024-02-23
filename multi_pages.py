import streamlit as st

# Create a function for each page
def home_page():
  st.title("Home Page")
  st.write("This is the home page.")

def about_page():
  st.title("About Page")
  st.write("This is the about page.")

# Create the main app
def main():
  # Add a selectbox to the sidebar
  page = st.sidebar.selectbox("Select a page", ["Home", "About"])

  # Display the selected page
  if page == "Home":
    home_page()
  elif page == "About":
    about_page()

# Run the main app
if __name__ == "__main__":
  main()
