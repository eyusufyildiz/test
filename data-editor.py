import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

# Define a function to be called when the data is changed
def on_change(df):
    # Update the dataframe
    #df['age'] += 1
    st.warning("Dataframe is changed")

# Display the data editor
edited_df = st.data_editor(df, on_change=on_change, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.code(st.session_state)
