import streamlit as st
import pandas as pd

# Create a dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Use the st.data_editor widget to allow users to edit the dataframe
edited_df = st.data_editor(df)

# Get the edited dataframe using st.session_state
edited_df = st.session_state['edited_df']

# Identify the rows that have been edited by comparing the edited dataframe with the original dataframe
edited_rows = edited_df[edited_df != df].index
