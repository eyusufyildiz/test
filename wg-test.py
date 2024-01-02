import streamlit as st
from python_wireguard import Key
import subprocess

def showing():
      if st.button("Baloons"):
            st.balloons()
      
      if st.button("snow"):
            st.snow()
      
      if st.button("toast"):
            st.toast('Berkehan & Bilge')

def wg_keys():
      private, public = Key.key_pair()
      jData = {"wg-Private-key":private, "wg-Public-key":public}
      st.json( jData )


def rsa_demo():
      from Crypto.PublicKey import RSA
      key = RSA.generate(2048)
      public_key = key.publickey().exportKey("PEM")
      private_key = key.exportKey("PEM")
      st.code(public_key)
      st.code(private_key)

def run_os_commands():
      cmds=["df -h", 
            "cat /etc/os-release", 
            "curl https://api.ipify.org ", 
            "curl ifconfig.me/all.json",
            "curl https://vpnstar.streamlit.app/",
            "pip list",
            "cat /proc/cpuinfo | grep proc",
            "hostname",
            "free -m"
            ]
      
      for cmd in cmds:
          st.markdown(f"* {cmd}")
          try:
                res = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
                st.code(res)
          except:
                pass


showing()
wg_keys()
run_os_commands()
