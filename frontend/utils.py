import json
import yaml
import numpy as np
import streamlit as st
from typing import Dict, List


def select_tab() -> str:
    st.sidebar.subheader("Select Display Tab")
    tabs = ['Main Gear', 'Arm Motors', 'Image Detection']
    tab = st.sidebar.radio(label="Options:", options=tabs)
    return tab


with open("frontend/output_config.yml") as file:
    output_config = yaml.load(file, yaml.FullLoader)

with open("frontend/input_config.yml") as file:
    input_config = yaml.load(file, yaml.FullLoader)


def create_output_message(mode: str, data: Dict[str, int]) -> List[int]:
    """
    generate a data package that will be sent to the arduino
    :param mode: what kind of data is this. each kind has it's own output json configuration
    :param data: data to be sent
    :return: data package as a list of bytes
    """
    key_mapping = output_config[mode]
    float2byte = lambda x: list(np.array(x).tobytes())
    output_data = []
    for key in data.keys():
        output_data.extend([ord(key_mapping[key]), float2byte(data[key])])
    return output_data


def parse_input_json(mode: str, data: Dict) -> Dict:
    if mode == "ARM_MOTORS":
        return {"Motor A Angle": 0, "Motor B Angle": 0, "Motor C Angle": 0, "Motor D Angle": 0, "Motor E Angle": 0, "Motor F Angle": 0, "Grabber Angle": 0}
    elif mode == "MAIN_MOTORS":
        return {"Motor A Speed": 3.14, "Motor B Speed": 1.96, "Motor A Angle": 190, "Motor B Angle": 220, "Acceleration": 0.88, "Compass Angle": 67, "Speed": 0.9, "Angular Acceleration": 0.05}
    key_mapping = input_config[mode]
    parsed_dictionary = {}
    for key in data.keys():
        data_entry = {key_mapping[key]: data[key]}
        parsed_dictionary.update(data_entry)
    return parsed_dictionary
