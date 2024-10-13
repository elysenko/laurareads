#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:26:38 2024

@author: ericlysenko
"""

import streamlit as st

st.title("James' Blog")


url = "https://elderjws.blogspot.com/"

# Set the desired height for the iframe (in pixels)
iframe_height = 600

# Create an iframe with the specified height
iframe_code = f"""
    <iframe src="{url}" width="100%" height="{iframe_height}" frameborder="0"></iframe>
"""
st.markdown(iframe_code, unsafe_allow_html=True)