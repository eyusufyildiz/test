import streamlit as st
import streamlit_antd_components as sac


sac.button(label="Click me")

sac.menu(items=[
    sac.MenuItem(label="Home"),
    sac.MenuItem(label="About"),
    sac.MenuItem(label="Contact"),
])

