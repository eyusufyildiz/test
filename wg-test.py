import streamlit as st
from python_wireguard import Key
import paramiko
import subprocess

def showing():
      col1, col2, col3 = st.columns(3)
      with col1:
            if st.button("Baloons"):
                  st.balloons()
      with col2:
            if st.button("snow"):
                  st.snow()
      with col3:
            if st.button("toast"):
                  st.toast('Berkehan & Bilge')

def wg_keys():
      private, public = Key.key_pair()
      jData = {"wg-Private-key":private, "wg-Public-key":public}
      st.json( jData )


def client_public_ip():
    # url = 'https://checkip.amazonaws.com'
    url = 'https://api.ipify.org?format=json'
    #url = "https://ifconfig.me/all.json"
    st.write(f"Running for {url}")
    script = (f'await fetch("{url}").then('
                'function(response) {'
                    'return response.json();'
                '})')
    try:
        result = st_javascript(script)
        #return result
        if isinstance(result, dict) and 'ip' in result:
            return result
    except:
        pass


def run_os_commands():
      cmds=["df -h", 
            "cat /etc/os-release", 
            "curl https://api.ipify.org ", 
            "curl ifconfig.me/all.json",
            "curl https://vpnstar.streamlit.app/",
            "pip list",
            "cat /proc/cpuinfo | grep proc",
            "hostname"
            #"free -m"
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
st.code( client_public_ip() )
run_os_commands()
