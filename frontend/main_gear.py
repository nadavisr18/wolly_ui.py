import time
import streamlit as st
# from communication import Comm
from typing import Tuple, Dict, Any

NUM_COLUMNS = 4
TEST_DATA = {"Motor A Speed": 3.14, "Motor B Speed": 1.96, "Motor A Angle": 190, "Motor B Angle": 220, "Acceleration": 0.88, "Compass Angle": 67, "Speed": 0.9, "Angular Acceleration": 0.05}
# comm = Comm()


def main_gear_tab():
    st.header("Main Motors Controls")
    motors_command = engine_control_sliders()
    st.header("Main Motors & Sensors")
    display = st.empty()
    while True:
        time.sleep(0.01)
        TEST_DATA[list(TEST_DATA.keys())[0]] += 1
        motor_data = TEST_DATA# comm.get_main_motors_data()
        display_engine_stats(display, motor_data)
        if isinstance(motors_command, tuple):
            # comm.send_main_motors_command(motor_a, motor_b)
            print(motors_command)
            motors_command = None


def engine_control_sliders() -> Tuple[int, int]:
    """
    create a slider and angle input for controlling the main motors
    :return: (motor speed, angle)
    """
    default = 0
    motor_speed = st.slider("Motors Speed", -100, 100, default, step=10)
    angle = st.number_input("Angle", min_value=-180, max_value=180, value=0)
    if st.button("SEND"):
        return motor_speed, angle


def display_engine_stats(display, motors_stats: Dict):
    """
    go over each key value pair in the motor stats dictionary and display them
    :param display: an empty streamlit object (required for having updating text fields)
    :param motors_stats: a dictionary with all the values from the arduino | key = human readable name | value = value from arduino
    """
    cols = display.beta_columns(NUM_COLUMNS)
    for i, (key, value) in enumerate(motors_stats.items()):
        cols[i%NUM_COLUMNS].subheader(key)
        cols[i%NUM_COLUMNS].text(value)
