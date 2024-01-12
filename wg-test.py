import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_javascript import st_javascript
import subprocess, sys

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
      qp = st.query_params

      # Display the query parameters
      st.write("Query Parameters:", qp)

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


st.title("Streamlit server tests:")
st.code(st.version.STREAMLIT_VERSION_STRING)
st.code(sys.version)
# hide_streamlit()

with st.expander("Collector"):
    collect()

with st.expander("Show"):
    showing()

with st.expander("client_public_ip"): 
    client_public_ip()

with st.expander("run_os_commands"):
    run_os_commands()

with st.expander("get_headers"):   
    get_headers()
