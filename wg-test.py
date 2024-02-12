import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_javascript import st_javascript
import subprocess, sys
import socket
import threading


def menu_exm():
	import streamlit as st
	from streamlit_option_menu import option_menu
	
	# 4. Manual item selection
	if st.session_state.get('switch_button', False):
	    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
	    manual_select = st.session_state['menu_option']
	else:
	    manual_select = None
	    
	selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
	    icons=['house', 'cloud-upload', "list-task", 'gear'], 
	    orientation="horizontal", manual_select=manual_select, key='menu_4')
	st.button(f"Move to Next {st.session_state.get('menu_option', 1)}", key='switch_button')
	selected4
	
	# 5. Add on_change callback
	def on_change(key):
	    selection = st.session_state[key]
	    st.write(f"Selection changed to {selection}")
	    
	selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
	                        icons=['house', 'cloud-upload', "list-task", 'gear'],
	                        on_change=on_change, key='menu_5', orientation="horizontal")
	selected5
	


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
            "pip list",
            "cat /proc/cpuinfo | grep proc",
            ]

      for cmd in cmds:
          st.caption(f"* $ {cmd}")
          try:
                res = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
                st.code(res)
          except:
                pass

def get_headers():
	from streamlit.web.server.websocket_headers import _get_websocket_headers
	headers = _get_websocket_headers()
	st.json(headers)


# Function to handle incoming data from the client
def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break  # Break the loop if no data is received
        st.write("Received data:", data)

    # Close the client socket when the loop ends
    client_socket.close()

# Function to start the socket server
def start_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    st.write(f"Server listening on {host}:{port}")

    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        st.write(f"Accepted connection from {addr}")

        # Start a new thread to handle the client's data
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()



def tb1():
    import pandas as pd
    data_df = pd.DataFrame(
        {
            "category": [
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
                "📊 Data Exploration",
            ],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "category": st.column_config.SelectboxColumn(
                "App Category",
                help="The category of the app",
                width="medium",
                options=[
                    "📊 Sec1",
                    "📈 Sec2",
                    "🤖 Sec3",
                ],
                required=True,
            )
        },
        hide_index=True,
    )


def tbl_test():
	import random
	import pandas as pd
	
	df = pd.DataFrame(
	    {
	        "name": ["Roadmap", "Extras", "Issues"],
	        "url": ["https://roadmap.streamlit.app", 
                    "https://extras.streamlit.app", 
                    "https://issues.streamlit.app"],
	        "stars": [random.randint(0, 1000) for _ in range(3)],
	        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
            "Secim": ""
	    }
	)
	st.dataframe(
	    df,
	    column_config={
	        "name": "App name",
	        "stars": st.column_config.NumberColumn(
	            "Github Stars",
	            help = "Number of stars on GitHub",
	            format = "%d ⭐",
	        ),
	        "url": st.column_config.LinkColumn("Application URL"),
	        "views_history": st.column_config.LineChartColumn(
	            "Views (past 30 days)", 
		        help="Son ziyaretler", 
		        y_min=0, y_max=5000
	        ),
            "Secim": st.column_config.SelectboxColumn(
	            "Secimler",
	            help = "Secenekler, sec birisini",
                width = "medium",
                options = [
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "🤖 LLM",
                ],
                required=True,
	        ),
	    },
	    hide_index=True,
	)	




st.title("Streamlit server tests:")
st.code(st.version.STREAMLIT_VERSION_STRING)
st.code(sys.version)
# hide_streamlit()

menu_exm()

st.write("----")

with st.expander("tb1"):
     tb1()

with st.expander("Table-test"):
    tbl_test()

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

with st.expander("Start Collector"):
      # Start the server when the user clicks the button
      if st.button("Start Server"):
            start_server("localhost", int(5000))
