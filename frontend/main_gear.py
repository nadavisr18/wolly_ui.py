from typing import Tuple, Dict, Any
import streamlit as st

NUM_COLUMNS = 4
TEST_DATA = {"Motor A Speed": 3.14, "Motor B Speed": 1.96, "Motor A Angle": 190, "Motor B Angle": 220, "Acceleration": 0.88, "Compass Angle": 67, "Speed": 0.9, "Angular Acceleration": 0.05}


def main_gear_tab(motor_data: Dict = None) -> Tuple[Any, Any]:
    st.header("Main Motors Controls")
    motors_command = engine_control_sliders()
    st.header("Main Motors & Sensors Logs")
    display_engine_stats(TEST_DATA)
    if isinstance(motors_command, tuple):
        return motors_command
    else:
        return None, None


def engine_control_sliders() -> Tuple[int, int]:
    default = 0
    total = st.slider("Both Motors", -100, 100, default, step=10)
    default_a = total
    default_b = total
    motor_a = st.slider('Motor A', -100, 100, default_a, step=10)
    motor_b = st.slider('Motor B', -100, 100, default_b, step=10)
    if st.button("SEND"):
        return motor_a, motor_b


def display_engine_stats(engine_stats: Dict):
    # with st.form(key='engine_stats'):
    cols = st.beta_columns(NUM_COLUMNS)
    for i, (key, value) in enumerate(engine_stats.items()):
        cols[i%NUM_COLUMNS].subheader(key)
        cols[i%NUM_COLUMNS].text(value)
