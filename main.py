from frontend import *

# TODO: implement parse_ins and parse_gps functions to turn their input string into a dictionary in communication.py
# TODO: fill out input_config.yml and output_config.yml according to the correct protocol


def main():
    tab = select_tab()
    if tab == 'Main Gear':
        main_gear_tab()
    elif tab == 'Arm Motors':
        arm_motors_tab()
    elif tab == 'Image Detection':
        pass


if __name__ == '__main__':
    main()
