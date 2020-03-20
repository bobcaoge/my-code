# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import random


class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rectangles = rects
        self.nums = self.get_nums()

    def get_nums(self):
        nums = []
        old = 0
        for rect in self.rectangles:
            old += (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            nums.append(old)
        return nums

    def pick(self):
        """
        :rtype: List[int]
        """
        ret = None
        for i, rect in enumerate(self.rectangles):
            point = [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]
            if not ret:
                ret = point
            else:
                if random.random()*self.nums[i] > self.nums[i-1]:
                    ret = point
        return ret



def main():
    s = Solution([[-2,-2,-1,-1],[1,0,3,0]])
    print(s.nums)
    print(s.pick())


if __name__ == "__main__":
    main()
