import streamlit as st
from streamlit_option_menu import option_menu

def menu(idx=0):
	with st.sidebar:
	    selected = option_menu("Menu", ["Home", 'Settings'], 
	        icons=['house', 'gear'], default_index=idx, key=idx)
	
	if selected == "Home":
	    st.write("home is where the heart is")
	else:
	    st.write("settings is my bettings")

sl = st.selectbox('Select', [0, 1])
menu(sl)
