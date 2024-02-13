import streamlit as st
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import folium_static


def menu(idx=0):
	with st.sidebar:
	    selected = option_menu("Menu", ["Home",  "Select on Map"], 
		icons=['house', 'gear'], default_index=idx, key=idx)
	
	if selected == "Home":
	    st.write("home is where the heart is")
	else:
	    st.title("Get Latitude and Longitude from Map")
	
	    # Create a map object using Folium
	    m = folium.Map(location=[0, 0], zoom_start=2)
	
	    # Display the map using Streamlit
	    folium_static(m)
	
	    # Get latitude and longitude coordinates on click   

def get_coordinates(m):
    # Function to get latitude and longitude coordinates on click
    m.add_child(folium.LatLngPopup())



sl = st.selectbox('Select', [0, 1])
menu(sl)
