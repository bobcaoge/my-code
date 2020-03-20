# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections
import math


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        if len(points) <= 1:
            return len(points)
        m = collections.defaultdict(int)
        ret = 0
        for i, (a, b) in enumerate(points):
            special = 1
            m.clear()
            for j in range(i+1, len(points)):
                if points[j] == points[i]:
                    special += 1
                    continue
                c, d = points[j]
                g = math.gcd(b-d, a-c)
                m[((b-d)/g, -(a-c)/g)] += 1
            ret = max(ret, special)
            if m:
                ret = max(max([x for _, x in m.items()])+special, ret)
        return ret


def main():
    s = Solution()
    # print(s.maxPoints([[1,1],[2,2],[3,3]]))
    # print(s.maxPoints([[1,1],[2,2],[1,1]]))
    # print(s.maxPoints([[1,1],[1,1]]))
    print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(s.maxPoints([[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]))
    print(s.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))


if __name__ == "__main__":
    main()
