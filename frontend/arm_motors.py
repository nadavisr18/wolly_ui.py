import time
import streamlit as st
from typing import Tuple, Dict, Union
from communication import Comm

NUM_COLUMNS = 4
TEST_DATA = {"Motor A Angle": 0, "Motor B Angle": 0, "Motor C Angle": 0, "Motor D Angle": 0, "Motor E Angle": 0, "Motor F Angle": 0, "Grabber Angle": 0}
# comm = Comm()


def arm_motors_tab():
    motors_control = arm_motor_controls()
    grabber_state = grabber()
    display = st.empty()
    while True:
        time.sleep(0.01)
        TEST_DATA['Motor A Angle'] += 1
        motor_data = TEST_DATA# comm.get_arm_data()
        display_motors_stats(display, motor_data)
        if isinstance(motors_control, tuple):
            # comm.send_arm_motor_command(*arm_motors_command)
            print("Motor Commands: ", motors_control)
            motors_control = None
        if isinstance(grabber_state, int):
            # comm.send_grabber_command(arm_motors_command)
            print("Grabber State: ", grabber_state)
            grabber_state = None


def arm_motor_controls() -> Tuple[int, int, int, int, int, int]:
    st.header("Motors")
    default = 0
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


def display_motors_stats(display, motors_stats: Dict):
    cols = display.beta_columns(NUM_COLUMNS)
    for i, (key, value) in enumerate(motors_stats.items()):
        cols[i % NUM_COLUMNS].subheader(key)
        cols[i % NUM_COLUMNS].text(value)
