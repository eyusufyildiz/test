import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim


def map():
    try:
        m = fl.Map()
        m.add_child(fl.LatLngPopup())
        map = st_folium(m, height=350, width=700)
        
        data = None
        if map.get("last_clicked"):
            data = ( map["last_clicked"]["lat"], map["last_clicked"]["lng"] )
            #st.write(data) # Writes to the app
            return data
    except:
        return None


def geo_reverse(lat, lon):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        geolocator = Nominatim(user_agent="geoapiIssNow")
        #location    = geolocator.reverse(str(lat) + ", " + str(lon))
        #location_en = geolocator.reverse(str(lat) + ", " + str(lon), language='en')
        location    = geolocator.reverse(f"{lat}, {lon}")
        location_en = geolocator.reverse(f"{lat}, {lon}", language='en')
        
        address = location.raw['address']
        address_en = location_en.raw['address']
        return address, address_en
    except:
        return None


def address():
    try:
        lat, lon  = map()
        lat, lot = "{:.4f}".format(lat), "{:.4f}".format(lon)
        st.write(lat, lot)
        if lat and lot and geo_reverse(lat, lon):
            st.text("Addess:")
            tbl = pd.json_normalize( geo_reverse(lat, lon) )
            geo_data = geo_reverse(lat, lon)
            country_info_en = geo_data[1]
            
            st.write( tbl )
            st.write( country_info_en )

            country_code = country_info_en.get('country_code')
            country      = country_info_en.get('country')
            state        = country_info_en.get('state')
            province     = country_info_en.get('province')
            city         = country_info_en.get('city')
            town         = country_info_en.get('town')
            
            if country_code: country_code = st.text_input("Country Code:", country_info_en.get('country_code'))
            if country     : country      = st.text_input("Country:", country_info_en.get('country'))
            if state       : state        = st.text_input("State:", country_info_en.get('state'))
            if province    : province     = st.text_input("Province:", country_info_en.get('province'))
            if city        : city         = st.text_input("City:", country_info_en.get('city'))
            if town        : town         = st.text_input("Town:", country_info_en.get('town'))
    except:
        return None
        
address()
