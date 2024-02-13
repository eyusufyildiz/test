import streamlit as st
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import folium_static


def menu(idx=0):
	with st.sidebar:
	    st.title("Get Latitude and Longitude from Map")
	
	    # Create a map object using Folium
	    m = folium.Map(location=[0, 0], zoom_start=2)
	
	    # Display the map using Streamlit
	    folium_static(m)
	
	    # Get latitude and longitude coordinates on click
	    get_coordinates(m)

	def get_coordinates(m):
	    # Function to get latitude and longitude coordinates on click
	    lat_lon = folium.LatLngPopup()
	    m.add_child(lat_lon)
	    st.write("Latitude and Longitude Coordinates:")
	    st.write(lat_lon)



sl = st.selectbox('Select', [0, 1])
menu(sl)
