import streamlit as st
from streamlit_option_menu import option_menu

# https://github.com/victoryhb/streamlit-option-menu
def menu_exm():
	# 5. Add on_change callback
	def on_change(key):
	    selection = st.session_state[key]
	    st.write(f"Selection changed to {selection}")
	    
	selected5 = option_menu("Welcome", ["Home", "Upload", "Tasks", 'Settings'],
	                        icons=['house', 'cloud-upload', "list-task", 'gear'],
	                        on_change=on_change, key='Tasks', orientation="horizontal")
	selected5
	

menu_exm()

st.write("----")
