import streamlit as st
import pandas as pd


# Create a dataframe
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Carol'], 'age': [25, 30, 35]})

# Define a function to be called when the data is changed
def on_change(df):
    # Update the dataframe
    df['age'] += 1

# Display the data editor
st.data_editor(df, on_change=on_change)

# Display the updated dataframe
st.write(df)
