import json
import yaml
from typing import List, Dict
from smbus2 import SMBus, i2c_msg

with open("communication/i2c_config.yml") as file:
    config = yaml.load(file, yaml.FullLoader)

MAIN_ARDUINO_ADDRESS = config['MAIN_ARDUINO_ADDRESS']
MAIN_ARDUINO_MESSAGE_LENGTH = config['MAIN_ARDUINO_MESSAGE_LENGTH']

ARM_ARDUINO_ADDRESS = config['ARM_ARDUINO_ADDRESS']
ARM_ARDUINO_MESSAGE_LENGTH = config['ARM_ARDUINO_MESSAGE_LENGTH']

GPS_ADDRESS = config['GPS_ADDRESS']
GPS_MESSAGE_LENGTH = config['GPS_MESSAGE_LENGTH']

INS_ADDRESS = config['INS_ADDRESS']
INS_MESSAGE_LENGTH = config['INS_MESSAGE_LENGTH']


class Comm:
    def __init__(self):
        self.bus = SMBus(1)

    def __del__(self):
        self.bus.close()

    def get_main_motors_data(self) -> Dict:
        """
        read data from main arduino, INS and GPS modules
        convert data to string and parse it into a dictionary object
        :return: json with data from arduino
        """
        arduino_message = i2c_msg.read(MAIN_ARDUINO_ADDRESS, MAIN_ARDUINO_MESSAGE_LENGTH)
        gps_message = i2c_msg.read(GPS_ADDRESS, GPS_MESSAGE_LENGTH)
        ins_message = i2c_msg.read(INS_ADDRESS, INS_MESSAGE_LENGTH)
        self.bus.i2c_rdwr(arduino_message, gps_message, ins_message)

        arduino_json = self.bytes_to_string(list(arduino_message))
        arduino_dict = json.loads(arduino_json)
        gps_message = self.bytes_to_string(list(arduino_message))
        gps_dict = self.parse_gps(gps_message)

        ins_message = self.bytes_to_string(list(arduino_message))
        ins_dict = self.parse_ins(ins_message)
        return arduino_dict.update(gps_dict).update(ins_dict)

    def get_arm_data(self) -> Dict:
        """
        read data from arm arduino
        convert data to string and parse it into a dictionary object
        :return: json with data from arduino
        """
        msg = i2c_msg.read(ARM_ARDUINO_ADDRESS, MAIN_ARDUINO_MESSAGE_LENGTH)
        self.bus.i2c_rdwr(msg)
        string_message = self.bytes_to_string(list(msg))
        return json.loads(string_message)

    def send_main_motors_command(self, output_message: str):
        msg = i2c_msg.write(MAIN_ARDUINO_ADDRESS, output_message)
        self.bus.i2c_rdwr(msg)

    def send_grabber_command(self, output_message: str):
        msg = i2c_msg.write(ARM_ARDUINO_ADDRESS, output_message)
        self.bus.i2c_rdwr(msg)

    def send_arm_motor_command(self, output_message: str):
        msg = i2c_msg.write(ARM_ARDUINO_ADDRESS, output_message)
        self.bus.i2c_rdwr(msg)

    @staticmethod
    def bytes_to_string(bytes_list: List[int]) -> str:
        string = ""
        for byte in bytes_list:
            string += chr(byte)
        return string

    @staticmethod
    def parse_gps(input_data: str):
        return input_data

    @staticmethod
    def parse_ins(input_data: str):
        return input_data
