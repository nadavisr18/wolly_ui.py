from typing import List, Tuple, Dict
from smbus2 import SMBus, i2c_msg

MAIN_ARDUINO_ADDRESS = 1
MAIN_ARDUINO_MESSAGE_LENGTH = 64
ARM_ARDUINO_ADDRESS = 2
ARM_ARDUINO_MESSAGE_LENGTH = 64


class Comm:
    def __init__(self):
        self.bus = SMBus(1)

    def __del__(self):
        self.bus.close()

    def get_main_motors_data(self) -> Dict:
        msg = i2c_msg.read(MAIN_ARDUINO_ADDRESS, MAIN_ARDUINO_MESSAGE_LENGTH)
        self.bus.i2c_rdwr(msg)
        return {}

    def send_main_motors_command(self, motor_a: int, motor_b: int):
        msg = i2c_msg.write(MAIN_ARDUINO_ADDRESS, [motor_a, motor_b])
        self.bus.i2c_rdwr(msg)

    def get_arm_data(self) -> Dict:
        msg = i2c_msg.read(ARM_ARDUINO_ADDRESS, MAIN_ARDUINO_MESSAGE_LENGTH)
        self.bus.i2c_rdwr(msg)
        return {}

    def send_grabber_command(self, command: int):
        msg = i2c_msg.write(ARM_ARDUINO_ADDRESS, [command])
        self.bus.i2c_rdwr(msg)

    def send_arm_motor_command(self, a: int, b: int, c: int, d: int, e: int, f: int):
        msg = i2c_msg.write(ARM_ARDUINO_ADDRESS, [a, b, c, d, e, f])
        self.bus.i2c_rdwr(msg)
