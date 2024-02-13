import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim


def map():
    m = fl.Map()
    m.add_child(fl.LatLngPopup())
    map = st_folium(m, height=350, width=700)
    
    data = None
    if map.get("last_clicked"):
        data = ( map["last_clicked"]["lat"], map["last_clicked"]["lng"] )
        #st.write(data) # Writes to the app
        return data


def geo_reverse(lat, lon):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")
    geolocator = Nominatim(user_agent="geoapiIssNow")
    location    = geolocator.reverse(str(lat) + ", " + str(lon))
    location_en = geolocator.reverse(str(lat) + ", " + str(lon), language='en')
    #location    = geolocator.reverse(f"{lat}, {lon}")
    #location_en = geolocator.reverse(f"{lat}, {lon}", language='en')
    
    try:
        address = location.raw['address']
        address_en = location_en.raw['address']
        return address, address_en
    except:
        return None


lat, lon = map()
lat, lot = "{:.4f}".format(lat), "{:.4f}".format(lon)
st.code([lat, lot])

if lat and lot and geo_reverse(lat, lon):
    st.text("Addess:")
    tbl = pd.json_normalize( geo_reverse(lat, lon) )
    st.write( tbl )
