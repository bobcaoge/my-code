# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        m = {}
        for row in wall:
            width = 0
            for brick in row:
                width += brick
                m[width] = m.get(width, 0)+1
        height = len(wall)
        m[sum(wall[0])] = 0
        ret = height
        for width, num in m.items():
            ret = min(ret, height-num)
        return ret


def main():
    s = Solution()
    print(s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))


if __name__ == "__main__":
    main()
