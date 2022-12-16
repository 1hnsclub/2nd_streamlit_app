from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.set_page_config(
  page_title="BearingPoint ESG Hub Demo App",
  page_icon="🌱📈📉"
  )

st.title("Welcome to BearingPoint's ESG HUB")
st.sidebar.success("Greenhouse Gas Emissions")
st.sidebar.success("Total Waste")
