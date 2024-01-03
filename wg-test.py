import streamlit as st
from streamlit_javascript import st_javascript
import subprocess

def hide_streamlit():
      hide_streamlit_style = """<style>
                  #MainMenu {visibility: hidden;}
                  footer {visibility: hidden;}
                  footer:after {
	                  content:'goodbye'; 
	                  visibility: visible;
	                  display: block;
	                  position: relative;
	                  #background-color: red;
	                  padding: 5px;
	                  top: 2px;
                  }
            </style>"""
      st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


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
	from python_wireguard import Key
	
	private, public = Key.key_pair()
	jData = {"wg-Private-key":private, "wg-Public-key":public}
	st.caption("WG-Keys:")
	st.json( jData )


def ssh_keys():
	import paramiko
	from paramiko import RSAKey
	from io import StringIO  
	
	# Generate a new key pair
	#key = paramiko.RSAKey.generate(bits=2048)
	#key.get_name()
	#key.get_base64
	
	# Generatees a public and private key
	key = paramiko.RSAKey.generate(2048)
	privateString = StringIO()
	key.write_private_key(privateString)
	st.caption("SSH-Keys:")
	st.code(key.get_base64())
	st.code(privateString.getvalue())
	

def client_public_ip():
    url = 'https://ifconfig.me/all.json'
    # url = 'https://api.ipify.org?format=json'
    st.caption("IP Headers:")
    script = (f'await fetch("{url}").then('
                'function(response) {'
                    'return response.json();'
                '})')
    try:
        result = st_javascript(script)
        #return result
        st.dataframe(result)
        #if isinstance(result, dict) and 'ip' in result:
        #    return result['ip']
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

hide_streamlit()
showing()
wg_keys()
ssh_keys()
client_public_ip()
run_os_commands()
