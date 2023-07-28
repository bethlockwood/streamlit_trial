# Import libraries
import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from PIL import Image
from helper_functions import id_from_url, album_results, album_upc

# Set page configuration to wide for primary desktop use
st.set_page_config(layout="wide")

# Create dashboard sections
header = st.container()
track_data = st.container()

# Display Spotify logo at the top of the sidebar
image = Image.open('Spotify_Logo_RGB_Green.png')
st.sidebar.image(image)

# Input boxes API login - ID & secret
client_id = st.secrets['spotify_api_creds']['client_id']
client_secret = st.secrets['spotify_api_creds']['client_secret']


# Set variables to 0 to be updated & allow display of containers when valid inputs are given by the user
auth_ready = 0
url_ready = 0


try:
    # Establish API connection with Spotipy
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client_id,
                                                        client_secret = client_secret))
    auth_ready = 1
except:
   with header:
    st.write('Please enter valid login credentials')
    auth_ready = 0
    
if auth_ready == 1:
    with header:
        #Text input for URL
        try:
            url = st.text_input("Enter URL:", "")
            url_type, id = id_from_url(url)

            # Validate that URL is a Spotify link for a playlist, ablum or track
            if url_type == 'album' or url_type == 'playlist' or url_type == 'track':
                url_ready = 1
            else:
                with track_data:
                    st.write('Enter a spotify URL for an Album, Playlist or Track')
                    url_ready = 0
        except:
            pass
        
if url_ready == 1:
    if url_type == 'album':
        album_info = album_results(sp,id)
        album_tracklist_info = album_info['tracks']['items']
        upc = album_upc(album_info)
        st.write(upc)