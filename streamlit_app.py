import streamlit as st
import pandas as pd
import numpy as np

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🏠")
page_1 = st.Page("catalogo_sismico_page.py", title="Page 1", icon="🌎")

# Set up navigation
pg = st.navigation([main_page, page_1])

# Run the selected page
pg.run()

