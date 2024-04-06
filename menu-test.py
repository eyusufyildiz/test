import streamlit as st
from streamlit_ant_design import st_ant_components

# Define Ant Design Menu
def ant_design_menu(default_selected_keys):
    return st_ant_components.menu(
        [
            {
                "title": "Menu 1",
                "key": "menu1",
                "sub_menu": [
                    {"title": "Option 1", "key": "option1"},
                    {"title": "Option 2", "key": "option2"},
                ],
            },
            {
                "title": "Menu 2",
                "key": "menu2",
                "sub_menu": [
                    {"title": "Option 3", "key": "option3"},
                    {"title": "Option 4", "key": "option4"},
                ],
            },
        ],
        default_selected_keys=default_selected_keys,
    )

# Main Streamlit app
def main():
    st.title('Streamlit with Ant Design Menu Example')

    # Define default selected keys for the menu
    default_selected_keys = ['option1']

    # Render Ant Design menu
    selected_keys = ant_design_menu(default_selected_keys)

    # Display selected keys
    st.write("Selected Keys:", selected_keys)

if __name__ == "__main__":
    main()
