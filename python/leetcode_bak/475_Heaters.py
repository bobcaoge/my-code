# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        houses.sort()
        i = r = 0
        for house in houses:
            while house >= sum(heaters[i:i+2])/2.:
                i += 1
            r = max(abs(house-heaters[i]), r)
        return r


def main():
    s = Solution()
    print(s.findRadius([1,2,3,5,15],[2,30]))
    print(s.findRadius([1,1,1,1,1,1,999,999,999,999],[499,500,501]))
    print(s.findRadius([1,2,3,4],[1,4]))
    a = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
    b = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
    print(s.findRadius(a, b))

    a = [474833169,264817709,998097157,817129560]
    b = [197493099,404280278,893351816,505795335]
    print(s.findRadius(a, b))
if __name__ == "__main__":
    main()
