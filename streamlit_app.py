import streamlit as st
import streamlit_functions as sf
# streamlit_app.py

import hmac
import streamlit as st

"""
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Main Streamlit app starts here
st.write("Here goes your normal Streamlit app...")
st.button("Click me")
"""

st.title("Resource Allocation 🩺")
st.write(
    "Click button below to query current worklist status:"
)


prototype_run = st.button("Get Data")

if prototype_run:
    sf.run_test()
