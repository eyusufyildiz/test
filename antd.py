import streamlit as st
import streamlit_antd_components as antd


antd.button(label="Click me")

antd.menu(items=[
    antd.MenuItem(label="Home"),
    antd.MenuItem(label="About"),
    antd.MenuItem(label="Contact"),
])

