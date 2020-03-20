# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def distributeCandies1(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        ret = 0
        old = -100001
        top = len(candies)/2
        candies.sort()
        for candy in candies:
            if candy == old:
                continue
            else:
                ret += 1
                old = candy
                if ret == top:
                    return ret
        return ret
    def distributeCandies2(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        ret = 0
        had = set()
        top = len(candies)/2
        for candy in candies:
            if candy in had:
                continue
            else:
                ret += 1
                had.add(candy)
                if ret == top:
                    return ret
        return ret
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        ret = 0
        had = {}
        top = len(candies)/2
        for candy in candies:
            if had.get(candy, 0) != 0:
                continue
            else:
                ret += 1
                had[candy] = 1
                if ret == top:
                    return ret
        return ret
def main():
    s = Solution()
    print(s.distributeCandies([1,2,2,2,4,3]))
    print(s.distributeCandies([1,1,1,1,2,2,2,3,3,3]))


if __name__ == "__main__":
    main()
