import streamlit as st
import streamlit_functions as sf

st.title("Clario 🩺")
st.write(
    "Click button below to query current worklist status:"
)


prototype_run = st.button("Get Data")

if prototype_run:
    sf.run_test()