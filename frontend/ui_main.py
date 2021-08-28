from frontend import *


def main():
    tab = select_tab()
    if tab == 'Main Gear':
        main_gear_tab()
    elif tab == 'Arm Motors':
        arm_motors_tab()
    elif tab == 'Image Detection':
        pass