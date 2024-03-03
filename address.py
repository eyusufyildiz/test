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
            #st.code(data) # Writes to the app
            return data
    except Exception as e:
        st.code(f"Error1: {str(e)}")


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
        map_data = folium_map()
        if map_data:
            lat, lon = map_data
            lat, lot = "{:.4f}".format(lat), "{:.4f}".format(lon)
            geo_data = geo_reverse(lat, lon)
            if geo_data:
                st.text("Location:")
                tbl = pd.json_normalize( geo_data )
                country_info_en = geo_data[1]
                
                country_code = country_info_en.get('country_code').upper()
                country      = country_info_en.get('country')
                county       = country_info_en.get('county')
                state        = country_info_en.get('state')
                province     = country_info_en.get('province')
                region       = country_info_en.get('region')
                district     = country_info_en.get('district')
                city         = country_info_en.get('city')
               #town         = country_info_en.get('town')
                
                #country_code = st.text_input("Country Code:", country_code)
                #country      = st.text_input("Country:", country)
                
                #if county    : county   = st.text_input("County:", county)    
                #if state     : state    = st.text_input("State:", state)
                #if region    : region   = st.text_input("Region:", region)
                #if province  : province = st.text_input("Province:", province)
                #if district  : district = st.text_input("District:", district)
                
                #city = st.text_input("City:", city)
                location_info = [country_code, country, county, state, region, province, district, city]
                vpn_survey_info = ", ".join( lc for lc in location_info if lc )
                st.write(vpn_survey_info)
                if st.button("Send"):
                    st.write("Sending...")
    except Exception as e:
        st.text(f"Error3: {str(e)}")
#######################

def c1():
    tab1, tab2 = st.tabs([ "Where would do you want a VPN server?", "Send your Comments..."])
    with tab1:
        st.write("""Click on map for where you want a VPN server.  I there isn't location ino cliek on another place.
                    Or, fill up form and send after click. 
                    We will add it to our VPN server lists asap.""")
        vpn_server_request()
    with tab2:
        #vpn_server_request()
        pass


c1()
