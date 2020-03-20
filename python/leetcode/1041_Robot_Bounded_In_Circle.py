# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
        self.x, self.y = 0, 0
        self.direction = NORTH
        self.m = {
            0:{
                "L": WEST,
                "R": EAST
            },
            1:{
                "L": NORTH,
                "R": SOUTH
            },
            2:{
                "L": EAST,
                "R": WEST
            },
            3:{
                "L": SOUTH,
                "R": NORTH
            },
        }
        dd = {
            0:[0, 1],
            1:[1, 0],
            2:[0, -1],
            3:[-1, 0],
        }
        def move(c):
            if c != "G":
                self.direction = self.m[self.direction][c]
            else:
                dx, dy = dd[self.direction]
                self.x += dx
                self.y += dy

        for c in instructions:
            move(c)
        if self.x == 0 and self.y == 0:
            return True

        return self.direction != NORTH


def main():
    s = Solution()
    print(s.isRobotBounded("GLRLLGLL"))
    print(s.isRobotBounded("GGLLGG"))
    print(s.isRobotBounded("GG"))
    print(s.isRobotBounded("GL"))


if __name__ == "__main__":
    main()
