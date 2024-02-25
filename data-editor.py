import streamlit as st
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [1, 2, 3, 4]})

col1, col2 = st.columns(2)
with col1:
    st.subheader("DataFrame")
    aa=st.data_editor( df, key="display1", disabled=("B"), )

with col2:
    st.subheader("after update")
    aa

st.write("Streamlit version: ", st.__version__)
