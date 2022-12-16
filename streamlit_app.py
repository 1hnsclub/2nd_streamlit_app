from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import snowflake.connector


st.set_page_config(
  page_title="BearingPoint ESG Hub Demo App",
  page_icon="🌱📈📉"
  )

st.title("Welcome to BearingPoint's ESG HUB")
st.sidebar.success("Greenhouse Gas Emissions")
st.sidebar.success("Total Waste")

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from ESG.PUBLIC.KPI_ACCESS_RULES;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")