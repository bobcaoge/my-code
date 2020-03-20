# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.insert(bisect.bisect(self.nums, num), num)

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.nums)
        if length% 2 == 0:
            return (self.nums[length//2] + self.nums[length//2-1]) / 2.0
        else:
            return self.nums[length//2]


def main():
    s = MedianFinder()
    s.addNum(1)
    print(s.findMedian())
    s.addNum(2)
    print(s.findMedian())
    s.addNum(3)
    print(s.findMedian())



if __name__ == "__main__":
    main()
