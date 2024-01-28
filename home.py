import streamlit as st
import utils
import os

st.title("piLab")

if st.button("Restart Network Services"):
    utils.restart_network_services()

if st.button("Restart System"):
    os.system("reboot")
