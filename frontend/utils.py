import streamlit as st


def select_tab() -> str:
    st.sidebar.subheader("Select Display Tab")
    tabs = ['Main Gear', 'Arm Motors', 'Image Detection']
    tab = st.sidebar.radio(label="Options:", options=tabs)
    return tab
