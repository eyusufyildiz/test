import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']
