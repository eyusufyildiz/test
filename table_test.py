import streamlit as st
import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Carol'], 'Age': [25, 30, 35]})

# Define a function to be called when the data editor is changed
def on_change():
    # Get the edited data
    edited_df = st.session_state.edited_df

    # Print the edited data
    st.write(edited_df)

# Display the data editor
st.data_editor(df, on_change=on_change)