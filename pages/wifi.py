import streamlit as st
import utils

data = utils.get_wifi_info()

st.title("WiFi Settings")
ssid = st.text_input('SSID' , data['ssid'])
wpa_passphrase = st.text_input('Password', data['wpa_passphrase'])
country_code = st.text_input('Country Code', data['country_code'])

if st.button("Save Changes"):
    utils.set_wifi_info('ssid', ssid)
    utils.set_wifi_info('wpa_passphrase', wpa_passphrase)
    utils.set_wifi_info('country_code', country_code)
    st.success("Changes saved")
