import streamlit as st
from python_wireguard import Key
import subprocess

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
      "apt list --installed"
      ]

for cmd in cmds:
    st.caption(cmd)
    try:
          res = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
          st.code(res)
    except:
          pass


st.balloons()
st.snow()
st.toast('Mr Stay-Puft')
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
