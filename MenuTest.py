import streamlit as st
from streamlit_option_menu import option_menu

def menu(idx=0):
	with st.sidebar:
	    selected = option_menu("Menu", ["Home",  "Select on Map"], 
	        icons=['house', 'gear'], default_index=idx, key=idx)
	
	if selected == "Home":
	    st.write("home is where the heart is")
	else:
		st.write("sSelect on Map")
		import folium
		
		# Create a map
		map = folium.map()
		
		# Add a marker to the map at the clicked location
		marker = folium.map.ClickForMarker()
		map.add_child(marker)
		
		# Get the latitude and longitude of the clicked location
		latitude = marker.location[0]
		longitude = marker.location[1]
		
		# Print the latitude and longitude
		print(latitude, longitude)     

sl = st.selectbox('Select', [0, 1])
menu(sl)
