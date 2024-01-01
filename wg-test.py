import streamlit as st
from python_wireguard import Key
import subprocess

if st.button("Baloons"):
      st.balloons()

if st.button("snow"):
      st.snow()

if st.button("toast"):
      st.toast('Berkehan & Bilge')

private, public = Key.key_pair()
st.write(f"Private-key: {private}")
st.write(f"Public-key: {public}")


cmds=["df -h", 
      "cat /etc/os-release", 
      "curl https://api.ipify.org ", 
      "pip list",
      "cat /proc/cpuinfo | grep proc",
      "hostname",
      "free -m",
      "curl https://vpnstar.streamlit.app/"
      ]

for cmd in cmds:
    st.markdown(f"* {cmd}")
    try:
          res = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
          st.code(res)
    except:
          pass



