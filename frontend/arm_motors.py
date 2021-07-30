from typing import Tuple, Dict, Union
import streamlit as st

NUM_COLUMNS = 4
TEST_DATA = {"Motor A Angle:": 0, "Motor B Angle:": 0, "Motor C Angle:": 0, "Motor D Angle:": 0, "Motor E Angle:": 0, "Motor F Angle:": 0, "Grabber Angle": 0}


def arm_motors_tab(motor_data: Dict = None) -> Union[int, Tuple[int, int, int, int, int, int]]:
    motors_control = arm_motor_controls()
    grabber_state = grabber()
    display_motors_stats(TEST_DATA)
    if motors_control is not None:
        a, b, c, d, e, f = motors_control
        return a, b, c, d, e, f
    if grabber_state is not None:
        return grabber_state


def arm_motor_controls() -> Tuple[int, int, int, int, int, int]:
    st.header("Motors")
    default = 0
    # if st.button("Reset Motors"):
    #     default = 0
    a = st.slider("Motor A", -100, 100, default, step=10)
    b = st.slider("Motor B", -100, 100, default, step=10)
    d = st.slider("Motor D", -100, 100, default, step=10)
    c = st.slider("Motor C", -100, 100, default, step=10)
    e = st.slider("Motor E", -100, 100, default, step=10)
    f = st.slider("Motor F", -100, 100, default, step=10)
    if st.button("SEND"):
        return a, b, c, d, e, f


def grabber() -> int:
    st.header("Grabber")
    col1, col2, col3 = st.beta_columns(3)
    output = None
    if col2.button("STOP"):
        output = 0
    if col1.button("OPEN"):
        output = -1
    if col3.button("CLOSE"):
        output = 1
    return output


def display_motors_stats(motors_stats: Dict):
    cols = st.beta_columns(NUM_COLUMNS)
    for i, (key, value) in enumerate(motors_stats.items()):
        cols[i % NUM_COLUMNS].subheader(key)
        cols[i % NUM_COLUMNS].text(value)
