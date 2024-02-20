import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import time


def map():
    try:
        m = fl.Map( tiles="cartodb positron" )
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
        
        geo_data = geo_reverse(lat, lon)
        
        if lat and lot and geo_data:
       #if lat and lot and geo_reverse(lat, lon):
            st.text("Addess:")
            tbl = pd.json_normalize( geo_data )
           #tbl = pd.json_normalize( geo_reverse(lat, lon) )
           #geo_data = geo_reverse(lat, lon)
            country_info_en = geo_data[1]
            
            # st.table( tbl )
            #st.write( country_info_en )

            country_code = country_info_en.get('country_code').upper()
            country      = country_info_en.get('country')
            county       = country_info_en.get('county')
            state        = country_info_en.get('state')
            province     = country_info_en.get('province')
            region       = country_info_en.get('region')
            district     = country_info_en.get('district')
            city         = country_info_en.get('city')
            #town         = country_info_en.get('town')
            
            country_code = st.text_input("Country Code:", country_code)
            country      = st.text_input("Country:", country)
            if county      : county       = st.text_input("County:", county)    
            if state       : state        = st.text_input("State:", state)
            if region      : region       = st.text_input("Region:", region)
            if province    : province     = st.text_input("Province:", province)
            if district    : district     = st.text_input("District:", district)
            city         = st.text_input("City:", city)
           #if town        : town         = st.text_input("Town:", town)

            #if st.button("Send"):
            vpn_survey_info = "|".join([ country_code, country, county, 
                                           state, region, province, district, city ])
            st.write(vpn_survey_info)
            
    except:
        return None
        
address()
