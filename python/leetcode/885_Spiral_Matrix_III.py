# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        self.m = {
            0 : [0, 1],
            1 : [1, 0],
            2 : [0, -1],
            3 : [-1, 0],

        }
        direction = 0
        self.ret = [[r0, c0]]
        count = 1
        self.row = R
        self.col = C

        while len(self.ret) < R*C:
            direction, r0, c0 = self.move(direction, count, r0, c0)
            direction, r0, c0 = self.move(direction, count, r0, c0)
            count += 1
        return self.ret

    def move(self, direction, count, x, y):
        for i in range(count):
            dx, dy = self.m[direction]
            x += dx
            y += dy
            if 0<= x < self.row and 0 <= y < self.col:
                self.ret.append([x, y])
        direction = (direction + 1)% 4
        return direction, x, y


def main():
    s = Solution()
    print(s.spiralMatrixIII(1,4,0,0))
    print(s.spiralMatrixIII(5,6,1,4))


if __name__ == "__main__":
    main()
