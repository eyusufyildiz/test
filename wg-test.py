import streamlit as st
from python_wireguard import Key

private, public = Key.key_pair()
st.write(f"Private-key: {private}")
st.write(f"Public-key: {public}")
