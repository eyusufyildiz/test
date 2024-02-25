import pandas as pd
import streamlit as st

# Create a dataframe
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Carol'], 'Age': [25, 30, 35]})

# Display the dataframe
st.dataframe(df)

# Add a data editor widget
edited_df = st.data_editor(df)

# Get the edited row
edited_row = edited_df[edited_df['Name'] == 'Alice']

# Display the edited row
st.write(edited_row)
