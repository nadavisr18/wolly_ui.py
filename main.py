from frontend import main as display_ui
from inverse_kinematics import InverseKinematics

# TODO: implement parse_ins and parse_gps functions to turn their input string into a dictionary in communication.py
# TODO: fill out input_config.yml and output_config.yml according to the correct protocol


def main():
    # point = (80, 100)
    # ik = InverseKinematics([0,0,0,0,0])
    # ik.reach(*point)
    # ik.show(*point)
    display_ui()

if __name__ == '__main__':
    main()
