import time
import streamlit as st
from .utils import parse_input_json, create_output_message
from communication import Comm
from typing import Tuple, Dict, Any

NUM_COLUMNS = 4
TEST_DATA = {"Motor A Speed": 3.14, "Motor B Speed": 1.96, "Motor A Angle": 190, "Motor B Angle": 220, "Acceleration": 0.88, "Compass Angle": 67, "Speed": 0.9, "Angular Acceleration": 0.05}
comm = Comm()


def main_gear_tab():
    """
    generates the arm tab
    first creates the main motors speed control slider
    then start the data receiving loop and update the next values on the screen every 0.01 seconds with info from the arduino
    """
    st.header("Main Motors Controls")
    motors_command = engine_control_sliders()
    st.header("Main Motors & Sensors")

    # st.empty lets you have a widget with static location on the page, so it can be updated instead of
    # adding a million widgets one under another
    display = st.empty()
    while True:
        time.sleep(0.01)
        TEST_DATA[list(TEST_DATA.keys())[0]] += 1
        raw_motor_data = comm.get_main_motors_data()
        motor_data = parse_input_json('MAIN_MOTORS', raw_motor_data)
        display_engine_stats(display, motor_data)

        # if there's new data motors_command will be dict, if there's no new data it will be None
        if isinstance(motors_command, dict):
            output_message = create_output_message('MAIN_MOTORS', motors_command)
            comm.send_main_motors_command(output_message)
            print(motors_command)
            motors_command = None


def engine_control_sliders() -> Dict[str, int]:
    """
    create a slider and angle input for controlling the main motors
    :return: (motor speed, angle)
    """
    default = 0
    motor_speed = st.slider("Motors Speed", -100, 100, default, step=10)
    angle = st.number_input("Angle", min_value=-180, max_value=180, value=0)
    if st.button("SEND"):
        return {"SPEED": motor_speed, "ANGLE": angle}


def display_engine_stats(display, motors_stats: Dict):
    """
    go over each key value pair in the motor stats dictionary and display them
    :param display: an empty streamlit object (required for updating text fields)
    :param motors_stats: a dictionary with all the values from the arduino | key = human readable name | value = value from arduino
    """
    cols = display.beta_columns(NUM_COLUMNS)
    for i, (key, value) in enumerate(motors_stats.items()):
        cols[i%NUM_COLUMNS].subheader(key)
        cols[i%NUM_COLUMNS].text(value)
