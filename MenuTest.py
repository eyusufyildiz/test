import streamlit as st
import folium
from streamlit_folium import folium_static


def main():
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
    st.write(lat_lon.to_json)

if __name__ == "__main__":
    main()
