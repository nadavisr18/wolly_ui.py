from math import cos, sin, atan2, pi


class Segment:
    def __init__(self, x: float, y: float, length: int, angle: float):
        """
        class representing an arm segment
        :param x: x coordinate of the base of the segment *CM*
        :param y: y coordinate of the base of the segment *CM*
        :param length: length of the segment *CM*
        :param angle: angle of the segment relative to straight forward along the plane of the arm, *RADIANS*
        """
        self.a = {"x": x, "y": y}
        self.length = length
        self.angle = angle

    def rotate(self, x: float, y: float):
        """
        make the segment point at a coordinate
        :param x: x of target
        :param y: y of target
        """
        self.angle = atan2(y-self.a['y'], x-self.a['x'])

    def translate(self, x: float, y: float):
        """
        make the segment's base move to a new coordinate
        :param x: new position in x direction
        :param y: new position in y direction
        """
        self.a['x'] = x
        self.a['y'] = y

    def touch(self, x: float, y: float):
        """
        translate the arm so it's endpoint touches the target point
        :param x: x position of target point
        :param y: y position of target point
        """
        opposite_angle = (self.angle+pi) % (2*pi)
        self.a['x'] = x+cos(opposite_angle) * self.length
        self.a['y'] = y+sin(opposite_angle) * self.length

    @property
    def b(self):
        """
        calculate the end point of the segment
        """
        b_x = self.a['x'] + cos(self.angle) * self.length
        b_y = self.a['y'] + sin(self.angle) * self.length
        return {"x": b_x, "y": b_y}
