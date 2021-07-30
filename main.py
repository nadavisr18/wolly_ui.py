from frontend import *
from communication import Comm

def main():
    tab = select_tab()
    if tab == 'Main Gear':
        motor_data = Comm.get_main_motors_data()
        motors_command = main_gear_tab()
        if isinstance(motors_command, tuple):
            motor_a, motor_b = motors_command
            Comm.send_main_motors_command(motor_a, motor_b)
    elif tab == 'Arm Motors':
        arm_data = Comm.get_arm_data()
        arm_motors_command = arm_motors_tab()
        # grabber command
        if isinstance(arm_motors_command, int):
            pass
            Comm.send_grabber_command(arm_motors_command)
        # arm motors command
        elif isinstance(arm_motors_command, tuple):
            pass
            Comm.send_arm_motor_command(*arm_motors_command)
    elif tab == 'Image Detection':
        pass

if __name__ == '__main__':
    main()