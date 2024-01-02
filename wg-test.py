import streamlit as st
from python_wireguard import Key
from Crypto.PublicKey import RSA
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


def generate_ssh_key_pair():
    # Generate an RSA key pair
    key = paramiko.RSAKey.generate(2048)

    # Get the private key string
    private_key = key.get_private_key().decode("utf-8")

    # Get the public key string
    public_key = key.get_base64()

    st.code(public_key)
    st.code(private_key)
    #return private_key, public_key

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
rsa_demo()
run_os_commands()
