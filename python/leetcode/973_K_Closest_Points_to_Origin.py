# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points = [[point[0]**2 + point[1]**2, point] for point in points]
        return [info[1] for info in sorted(points)[:K]]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
