# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import random
from math import cos, sin


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.x = x_center
        self.y = y_center
        self.radius = radius

    def randPoint(self):
        """
        :rtype: List[float]
        """
        length = random.random()*self.radius
        angel = random.random()*360
        return [length*cos(angel), length*sin(angel)]
    def randPoint_1(self):
        """
        :rtype: List[float]
        """

        x_ret = random.random()*2*self.radius - self.radius + self.x
        y_ret = random.random()*2*self.radius - self.radius + self.y
        while (x_ret-self.x)**2 + (y_ret-self.y)**2 > self.radius**2:
            x_ret = random.random()*2*self.radius - self.radius + self.x
            y_ret = random.random()*2*self.radius - self.radius + self.y
        return [x_ret, y_ret]




def main():
    s = Solution()


if __name__ == "__main__":
    main()
