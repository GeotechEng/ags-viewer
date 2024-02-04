import streamlit as st
from streamlit.logger import get_logger
import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import geodatasets

st.set_page_config(
    page_title="AGS4 Report Page",
    page_icon="👋",
)

st.write("# AGS4 Report Page")

chicago = gpd.read_file(geodatasets.get_path("geoda.chicago_commpop"))
groceries = gpd.read_file(geodatasets.get_path("geoda.groceries"))

st.dataframe(chicago)

map = chicago.plot()
st.pyplot(map)