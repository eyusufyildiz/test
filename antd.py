
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

if sac.buttons( items=["btn1"]):
    print("BTN1")


from streamlit_antd_components import menu, MenuItem

item = menu([
    MenuItem('menu1', icon='house'),
    MenuItem('menu2', icon='app', children=[
        MenuItem('menu3', icon='twitter'),
        MenuItem('disabled', disabled=True),
    ]),
], format_func='title', open_all=True)
st.write(f'The selected menu label is: {item}')

