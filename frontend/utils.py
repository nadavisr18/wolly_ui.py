import json
import yaml
import streamlit as st
from typing import Dict


def select_tab() -> str:
    st.sidebar.subheader("Select Display Tab")
    tabs = ['Main Gear', 'Arm Motors', 'Image Detection']
    tab = st.sidebar.radio(label="Options:", options=tabs)
    return tab


with open("frontend/output_config.yml") as file:
    output_config = yaml.load(file, yaml.FullLoader)

with open("frontend/input_config.yml") as file:
    input_config = yaml.load(file, yaml.FullLoader)


def create_output_message(mode: str, data: Dict) -> str:
    """
    generate a dictionary that will be sent to the arduino
    :param mode: what kind of data is this. each kind has it's own output json configuration
    :param data: data to be sent
    :return:
    """
    key_mapping = output_config[mode]
    output_data = {}
    for key in data.keys():
        data_entry = {key_mapping[key]: data[key]}
        output_data.update(data_entry)
    return json.dumps(output_data)


def parse_input_json(mode: str, data: Dict) -> Dict:
    key_mapping = input_config[mode]
    parsed_dictionary = {}
    for key in data.keys():
        data_entry = {key_mapping[key]: data[key]}
        parsed_dictionary.update(data_entry)
    return parsed_dictionary
