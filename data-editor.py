import streamlit as st
import pandas as pd

# Sample dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Display the dataframe and enable editing
edited_df = st.dataframe(df, height=300)
edited_df.data_editor()

# Get the rows that have been edited
edited_rows = edited_df.edited_rows
st.write('Edited Rows:', edited_rows)

# Display the updated dataframe
st.write('Updated DataFrame:', edited_df)
