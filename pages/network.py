import streamlit as st
import utils

data = utils.get_dhcpcd_info()

st.title("Network Settings")
ip_address = st.text_input('Router Address', data['ip_address'])
dns_servers = st.text_input('DNS Servers', data['dns_servers'].replace(' ', ', '))

if st.button("Save Changes"):
    utils.set_dhcpcd_info('static ip_address', ip_address)
    utils.set_dhcpcd_info('static domain_name_servers', dns_servers.replace(',',''))

    st.success("Changes saved")