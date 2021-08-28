import yaml
from math import sqrt, acos, atan2
from typing import List, Iterable
from .segment import Segment
import matplotlib.pyplot as plt
from matplotlib.patches import Arrow, Circle

BASE_X = 0
BASE_Y = 0


class InverseKinematics:
    def __init__(self, angles: List[float]):
        with open("inverse_kinematics/config.yml") as file:
            self.config = yaml.load(file, yaml.FullLoader)
        self.segments = []
        last_end_x = BASE_X
        last_end_y = BASE_Y
        for seg_length, angle in zip(self.config['Segments'], angles):
            segment = Segment(last_end_x, last_end_y, seg_length, angle)
            self.segments.append(segment)
            last_end_x = segment.b['x']
            last_end_y = segment.b['y']

    def reach(self, x: float, y: float):
        """
        make the arm touch the target point (x,y)
        :param x: target x
        :param y: target y
        """
        # make the arm touch the target (allowing the base of the arm to move as well)
        for i in range(len(self.segments) - 1, -1, -1):
            segment = self.segments[i]
            segment.rotate(x, y)
            segment.touch(x, y)
            x, y = segment.a.values()

        # a little bit of weird math so I'm gonna try to explain what I did. this is to make sure the base of the arm stays fixed
        #
        # mid point between the base of the arm and the beginning of segment 3
        ao = self.dist((BASE_X, BASE_Y), tuple(self.segments[2].a.values()))/2
        # the perfect angle for segment 1 so that the start of segment 2 will be at an equal distance
        # from the base of the arm and from the start of segment 3. *THIS ONLY WORKS IF SEGMENTS 1 AND 2 ARE THE SAME LENGTH*
        correct_angle = acos(ao/self.segments[0].length) + atan2(self.segments[2].a['y'] - BASE_Y, self.segments[2].a['x'] - BASE_X)
        # move segments 1 to the base of the arm and align itself with the correct angle
        self.segments[0].angle = correct_angle
        self.segments[0].translate(BASE_X, BASE_Y)
        # move segment 2 to connect with segment 1 and segment 3
        self.segments[1].translate(*self.segments[0].b.values())
        self.segments[1].rotate(*self.segments[2].a.values())

    def show(self, x: float, y: float):
        """
        display the arm in a sketch
        :param x: target x
        :param y: target y
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        base = Circle((BASE_X, BASE_Y), color='black', radius=2)
        ax.add_patch(base)
        for i, segment in enumerate(self.segments):
            print(segment.b, segment.angle)
            rect = Arrow(*segment.a.values(), segment.b['x'] - segment.a['x'], segment.b['y'] - segment.a['y'], width=6)
            ax.add_patch(rect)
        target = Circle((x, y), color='red', radius=2)
        ax.add_patch(target)
        plt.xlim([-50, 100])
        plt.ylim([-50, 100])
        plt.show()

    @staticmethod
    def dist(p1: Iterable, p2: Iterable) -> float:
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
