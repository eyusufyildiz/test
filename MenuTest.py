import folium as fl
from streamlit_folium import st_folium
import streamlit as st


m = fl.Map()
m.add_child(fl.LatLngPopup())
map = st_folium(m, height=350, width=700)

data = None
if map.get("last_clicked"):
    data = [map["last_clicked"]["lat"], map["last_clicked"]["lng"] ]

if data is not None:
    st.write(data) # Writes to the app
    print(data) # Writes to terminal
