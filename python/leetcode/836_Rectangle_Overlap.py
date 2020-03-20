# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec2[0] >= rec1[2] or rec2[1] >= rec1[3] or rec2[2] <= rec1[0] or rec2[3] <= rec1[1])
    def isRectangleOverlap1(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1, x2, y2 = rec1
        x11,y11, x22, y22 = rec2
        return not (x11 >= x2 or y11 >= y2 or x22 <= x1 or y22 <= y1)

def main():
    s = Solution()


if __name__ == "__main__":
    main()
