# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        s = set()
        points = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i):
                s.add((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
        if len(s) != 2:
            return False
        return min(s)*2 == max(s)


def main():
    s = Solution()
    print(s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))


if __name__ == "__main__":
    main()
