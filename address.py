import streamlit as st

import time

import folium as fl
from streamlit_folium import st_folium
import pandas as pd
from geopy.geocoders import Nominatim


################################
def folium_map():
    try:
        m = fl.Map( tooltip="Coast")
        m.add_child(fl.LatLngPopup())
        map = st_folium(m, height=350, width=700)
        
        if map.get("last_clicked"):
            data = ( map["last_clicked"]["lat"], map["last_clicked"]["lng"] )
            st.code(data) # Writes to the app
            return data
    except Exception as e:
        st.code(f"Error1: {str(e)}")
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
    except Exception as e:
        st.code(f"Error2: {str(e)}")


def vpn_server_request():
    try:
        lat, lon = folium_map()
        lat, lot = "{:.4f}".format(lat), "{:.4f}".format(lon)
        geo_data = geo_reverse(lat, lon)

        st.code(geo_data)
        
        if lat and lot and geo_data:
            st.text("Addess:")
            tbl = pd.json_normalize( geo_data )
            country_info_en = geo_data[1]
            
            country_code = country_info_en.get('country_code', "").upper()
            country      = country_info_en.get('country', "")
            county       = country_info_en.get('county', "")
            state        = country_info_en.get('state', "")
            province     = country_info_en.get('province', "")
            region       = country_info_en.get('region', "")
            district     = country_info_en.get('district', "")
            city         = country_info_en.get('city', "")
           #town         = country_info_en.get('town')
            
            location_info = [country_code, country, county, state, region, province, district, city]
            st.write(location_info)
            
            country_code = st.text_input("Country Code:", country_code)
            country      = st.text_input("Country:", country)
            
            if county    : county   = st.text_input("County:", county)    
            if state     : state    = st.text_input("State:", state)
            if region    : region   = st.text_input("Region:", region)
            if province  : province = st.text_input("Province:", province)
            if district  : district = st.text_input("District:", district)
            
            city = st.text_input("City:", city)
    
            #if st.button("Send"):
            vpn_survey_info = " | ".join( location_info )
            st.write(vpn_survey_info)
    except Exception as e:
        st.text(f"Error3: {str(e)}")
#######################

def c1():
    tab1, tab2 = st.tabs([ "Where would do you want a VPN server?", "Send your Comments..."])
    with tab1:
        #folium_map()
        lat, lon = folium_map()
        lat, lot = "{:.4f}".format(lat), "{:.4f}".format(lon)
        geo_data = geo_reverse(lat, lon)

        st.code(geo_data)
                st.write("Click on map for where you want a VPN server. Or, fill up form and send after click. We will add it to our VPN server lists asap.")

    with tab2:
        #vpn_server_request()


c1()
