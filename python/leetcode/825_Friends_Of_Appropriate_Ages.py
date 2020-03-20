# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        ret = 0
        for i, age in enumerate(ages):
            left = bisect.bisect(ages, (age >> 1) + 7)
            right = bisect.bisect(ages, age)
            ret += right-left-1 if right > left else 0
        return ret




def main():
    s = Solution()
    # print(s.numFriendRequests([16,16]))
    # print(s.numFriendRequests([16,17,18]))
    # print(s.numFriendRequests([20,30,100,110,120]))
    print(s.numFriendRequests([108,115,5,24,82]))


if __name__ == "__main__":
    main()
