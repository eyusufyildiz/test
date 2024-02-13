
import folium as fl
from streamlit_folium import st_folium
import streamlit as st

def get_pos(lat,lng):
    return lat,lng

m = fl.Map()

m.add_child(fl.LatLngPopup())

map = st_folium(m, height=350, width=700)


data = get_pos(map['last_clicked']['lat'],map['last_clicked']['lng'])

if data is not None:
    st.write(data)
