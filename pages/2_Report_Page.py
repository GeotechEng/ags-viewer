import streamlit as st
from streamlit.logger import get_logger
import numpy as np
import pandas as pd
import python_ags4
from python_ags4 import AGS4

st.set_page_config(
    page_title="AGS4 Report Page",
    page_icon="👋",
)

st.write("# AGS4 Report Page")

from python_ags4.data import load_test_data
tables, headings = load_test_data()
LOCA = AGS4.convert_to_numeric(tables['LOCA'])


st.dataframe(LOCA)