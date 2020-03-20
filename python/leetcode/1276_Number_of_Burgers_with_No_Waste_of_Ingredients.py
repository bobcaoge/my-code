# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        x, y = (tomatoSlices-2*cheeseSlices)//2, (4*cheeseSlices-tomatoSlices)//2
        if x+y == cheeseSlices and 4*x+2*y== tomatoSlices and x >= 0 and y >= 0:
            return [x, y]
        return []


def main():
    s = Solution()
    print(s.numOfBurgers(tomatoSlices = 16, cheeseSlices = 7))


if __name__ == "__main__":
    main()
