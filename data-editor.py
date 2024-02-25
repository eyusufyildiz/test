import streamlit as st
import pandas as pd

# Sample dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Display the editable dataframe
edited_df = st.beta_editable_dataframe(df)

# Get the rows that have been edited
edited_rows = st.button("Get Edited Rows")
if edited_rows:
    st.write('Edited Rows:', edited_df)

# Display the updated dataframe
st.write('Updated DataFrame:', edited_df)

