import streamlit as st
import streamlit_functions as sf

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


prototype_run = st.button("Prototype")

if prototype_run:
    sf.run_test()