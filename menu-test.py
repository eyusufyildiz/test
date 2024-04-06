import streamlit as st

# Define Ant Design Menu using HTML/CSS
def ant_design_menu():
    st.markdown("""
    <style>
        .ant-menu {
            background-color: #f0f2f5;
            padding: 16px;
            border-radius: 4px;
            width: 200px;
        }
        .ant-menu-item {
            margin-bottom: 8px;
        }
    </style>
    
    <div class="ant-menu">
        <div class="ant-menu-item">Menu 1</div>
        <div class="ant-menu-item">Option 1</div>
        <div class="ant-menu-item">Option 2</div>
        <div class="ant-menu-item">Menu 2</div>
        <div class="ant-menu-item">Option 3</div>
        <div class="ant-menu-item">Option 4</div>
    </div>
    """)

# Main Streamlit app
def main():
    st.title('Streamlit with Ant Design Menu Example')

    # Render Ant Design menu
    ant_design_menu()

if __name__ == "__main__":
    main()
