# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def judge(self, grid, start, end):
        ret = (True, grid[start][start])
        for i in range(start, end+1):
            for j in range(start, end+1):
                if grid[i][j] != ret[-1]:
                    return False, 0
        return ret

    def buffer(self,root, grid, x1, y1, x2, y2):
        mid_from_top_to_down = int((y1+y2)/2)
        mid_from_left_to_right = int((x1+x2)/2)
        # 区域划分
        # TopLeft(start, mid)

        # TopRight(
        # BottomLeft
        # BottomRight



    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """


def main():
    s = Solution()


if __name__ == "__main__":
    main()
