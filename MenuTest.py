import folium as fl
from streamlit_folium import st_folium
import streamlit as st
from geopy.geocoders import Nominatim

def map():
    m = fl.Map()
    m.add_child(fl.LatLngPopup())
    map = st_folium(m, height=350, width=700)
    
    data = None
    if map.get("last_clicked"):
        data = (map["last_clicked"]["lat"], map["last_clicked"]["lng"] )
    
    if data is not None:
        st.write(data) # Writes to the app
        return data




geolocator = Nominatim(user_agent="geoapiExercises")
def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country
    
#print(city_state_country("47.470706, -99.704723"))
st.code(city_state_country( map() ))

