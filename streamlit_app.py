import streamlit as st
import streamlit_functions as sf
# streamlit_app.py

import hmac
import streamlit as st

st.title("Resource Allocation 🩺")
st.write(
    "Click button below to query current worklist status:"
)


prototype_run = st.button("Get Data")

if prototype_run:
    sf.run_test()
