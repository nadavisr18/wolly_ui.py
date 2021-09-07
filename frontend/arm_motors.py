import time
import streamlit as st
from communication import Comm
from typing import Tuple, Dict, Union
from .utils import create_output_message, parse_input_json, output_config

NUM_COLUMNS = 4
comm = Comm()


def arm_motors_tab():
    """
    generates the arm tab
    first creates a slider for each arm motor
    then creates buttons for grabber control
    then start the data receiving loop and update the next values on the screen every 0.01 seconds with info from the arduino
    """
    motors_control = arm_motor_controls()
    grabber_state = grabber()

    # st.empty lets you have a widget with static location on the page, so it can be updated instead of
    # adding a million widgets one under another
    display = st.empty()
    while True:
        time.sleep(1/output_config['FPS'])
        raw_motor_data = ""#comm.get_arm_data()
        motor_data = parse_input_json('ARM_MOTORS', raw_motor_data)
        display_motors_stats(display, motor_data)

        # if there's new data motors_control will be a dict, if there's no new data it will be None
        if isinstance(motors_control, dict):
            message = create_output_message("ARM_MOTORS", motors_control)
            print(message)
            comm.send_arm_motor_command(message[:7])
            motors_control = None

        # if there's new data grabber_state will be dict, if there's no new data it will be None
        if isinstance(grabber_state, dict):
            message = create_output_message("GRABBER_COMMAND", grabber_state)
            print(message)
            comm.send_arm_motor_command(message)
            grabber_state = None


def arm_motor_controls() -> Dict[str, int]:
    """
    create 6 sliders, one for each arm motor
    :return: 6 int values, one for each arm motor
    """
    st.header("Motors")
    default = 0
    a = st.slider("Motor A", -100, 100, default, step=10)
    b = st.slider("Motor B", -100, 100, default, step=10)
    d = st.slider("Motor D", -100, 100, default, step=10)
    c = st.slider("Motor C", -100, 100, default, step=10)
    e = st.slider("Motor E", -100, 100, default, step=10)
    if st.button("SEND"):
        return {"A": a, "B": b, "C": c, "D": d, "E": e}


def grabber() -> dict:
    """
    create 3 buttons for controlling the grabber
    :return: 0 for STOP | 1 for CLOSE | -1 for OPEN
    """
    st.header("Grabber")
    col1, col2, col3 = st.beta_columns(3)
    output = None
    if col2.button("STOP"):
        output = 0
    if col1.button("OPEN"):
        output = -1
    if col3.button("CLOSE"):
        output = 1
    if isinstance(output, int):
        return {"GRABBER_STATE": output}


def display_motors_stats(display, motors_stats: Dict):
    """
    go over each key value pair in the motor stats dictionary and display them
    :param display: an empty streamlit object (required for having updating text fields)
    :param motors_stats: a dictionary with all the values from the arduino | key = human readable name | value = value from arduino
    """
    cols = display.beta_columns(NUM_COLUMNS)
    for i, (key, value) in enumerate(motors_stats.items()):
        cols[i % NUM_COLUMNS].subheader(key)
        cols[i % NUM_COLUMNS].text(value)
