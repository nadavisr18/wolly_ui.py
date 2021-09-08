from frontend import main as display_ui
from inverse_kinematics import InverseKinematics

# TODO: ARM COMMS & CONTROL (IK)
# TODO: INS & GPS
# TODO: MAIN MOTORS
# TODO: IMAGE RECOGNITION


def main():
    # point = (80, 100)
    # ik = InverseKinematics([0,0,0,0,0])
    # ik.reach(*point)
    # ik.show(*point)
    display_ui()

if __name__ == '__main__':
    main()
