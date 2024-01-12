import streamlit as st
from streamlit_option_menu import option_menu
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


def collect():
   if st.button("Collect data:"):
      # Get the query parameters
      qp = st.query_params()

      # Display the query parameters
      st.write("Query Parameters:", qp)

      # Access specific query parameters
      param_value = query_params.get("param_name", "default_value")
      st.write("Value of 'param_name':", param_value)


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
      st.code( str(private) )
      st.code( str(public ) )

def ssh_keys():
	import paramiko, os
	from paramiko import RSAKey
	from io import StringIO  
  
	path = os.getcwd() 
	dir_list = os.listdir(path) 
	st.code(f"Files and directories in {path}: \n {dir_list}") 

	# Generatees a public and private key
	key = paramiko.RSAKey.generate(2048)
	privateString = StringIO()
	key.write_private_key(privateString)
	st.caption("SSH-Keys:")
	st.code(key.get_base64())
	st.code(privateString.getvalue())

#def create_ssh_keypair(comment=None, bits=2048):
#    """Generate an ssh keypair for use on the overcloud"""
#    if comment is None:
#        comment = "Generated by Yusuf Yildiz"
#    key = paramiko.RSAKey.generate(bits)
#    keyout = StringIO()
#    key.write_private_key(keyout)
#    private_key = keyout.getvalue()
#    public_key = '{} {} {}'.format(key.get_name(), key.get_base64(), comment)
#    st.caption("SSH keys by paramiko")
#    st.code({
#        'private_key': private_key,
#        'public_key': public_key,
#    })

def client_public_ip():
    url = 'https://ifconfig.me/all.json'
    # url = 'https://api.ipify.org?format=json'
    st.caption(url)
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

def get_headers():
	from streamlit.web.server.websocket_headers import _get_websocket_headers
	headers = _get_websocket_headers()
	st.json(headers)


def menu():
      opt = st.selectbox('--> Select', ["public", "admin", "user"])
      st.title(f"{opt} is selected..")

      public_menu = ["client_public_ip"]
      admin_menu  = ["wg_keys", "ssh_keys"]
      user_menu   = ["run_os_commands", 'get_headers']

      with st.sidebar:
            if   opt == "public": mn_list = public_menu
            elif opt == "admin": mn_list = admin_menu
            elif opt == "user": mn_list = user_menu

            selected = option_menu(None,  mn_list, 
                  #icons=['geo-alt', 'cloud-upload', "list-task", 'gear', 'broadcast-pin'], 
                  menu_icon = "gear",
                  #default_index=0
            )

      if selected == "wg_keys": wg_keys()

      
      elif selected == "ssh_keys": ssh_keys()
      elif selected == "client_public_ip": client_public_ip()
      elif selected == 'run_os_commands': run_os_commands()
      elif selected == 'get_headers': get_headers()
      

st.title("Streamlit server tests:")
# hide_streamlit()
collect()
menu()
