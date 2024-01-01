import streamlit as st
from python_wireguard import Key
import subprocess

private, public = Key.key_pair()
st.write(f"Private-key: {private}")
st.write(f"Public-key: {public}")


cmds=["df -h", "cat /etc/os-release", "sudo apt install wireguard" ]

for cmd in cmds:
    res = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    st.code(res)
