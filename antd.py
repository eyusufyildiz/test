import streamlit as st
import streamlit_antd_components as sac


import streamlit as st
import streamlit_antd_components as sac

btn = sac.buttons(
    items=['button1', 'button2', 'button3'],
    index=0,
    format_func='title',
    align='center',
    direction='horizontal',
    radius='lg',
    return_index=False,
)
st.write(f'The selected button label is: {btn}')


a=sac.buttons(label="Click me", items=["btn1"])
# 
# sac.menu(items=[
#     sac.MenuItem(label="Home"),
#     sac.MenuItem(label="About"),
#     sac.MenuItem(label="Contact"),
# ])

