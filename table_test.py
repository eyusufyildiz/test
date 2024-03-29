import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
        "stock": [20, 55, 67, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ProgressColumn("Sales volume", help="The sales volume in USD",  min_value=0, max_value=1000),
        "stock": st.column_config.ProgressColumn("stock volume", help="TNum of stock",  min_value=0, max_value=100),
    },
    hide_index=True,
)
