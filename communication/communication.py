from typing import List, Tuple
from smbus2 import SMBus, i2c_msg

MAIN_ARDUINO_ADDRESS = 1
MAIN_ARDUINO_MESSAGE_LENGTH = 64
ARM_ARDUINO_ADDRESS = 2
ARM_ARDUINO_MESSAGE_LENGTH = 64


class Comm:
    @classmethod
    def get_main_motors_data(cls) -> List[int]:
        msg = i2c_msg.read(MAIN_ARDUINO_ADDRESS, MAIN_ARDUINO_MESSAGE_LENGTH)
        with SMBus(1) as bus:
            bus.i2c_rdwr(msg)
        return list(msg)
