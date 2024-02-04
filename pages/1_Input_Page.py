import streamlit as st
from streamlit.logger import get_logger
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="AGS4 Input Page",
    page_icon="👋",
)

st.write("# AGS4 Input Page")

st.markdown(
    """
Notes 
- The tool app works with AGS4 files only 
- select an AGS4 file using the file selection button 
- Select the headers within the file that contain the Eastings, Northings or Latitude and Longitude
- Select the Coordinate Reference System (CRS) for the coordinates the uses
- Select the header containing the elevation 
- Run the file, results are presented in the Report Page tab 
"""
)