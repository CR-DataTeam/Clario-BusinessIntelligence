import streamlit as st
import streamlit_functions as sf
# streamlit_app.py

import hmac
import streamlit as st
st. set_page_config(layout="wide")
st.logo('usrc_inverted.png')
st.title("Resource Allocation 🩺")
st.write(
    "Click button below to query current worklist status:"
)


prototype_run = st.button("Get Data")

if prototype_run:
    sf.run_test()
