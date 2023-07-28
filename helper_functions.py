import re
import streamlit as st

def id_from_url(url):
    try:
        url_regex = re.search(r"^https?:\/\/(?:open\.)?spotify.com\/(user|episode|playlist|track|album)\/(?:spotify\/playlist\/)?(\w*)", url)

        return url_regex.group(1), url_regex.group(2)

    except AttributeError:
        return 'invalid URL'
    
def album_results(sp,id):
    return sp.album(id, market = 'GB')


@st.cache_data
def album_upc(album_info):
    try:
        upc = album_info['external_ids'].get('upc')
    except:
        upc = "NULL"
    return upc