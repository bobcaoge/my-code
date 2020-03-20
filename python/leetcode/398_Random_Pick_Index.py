# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.m = self.manage()

    def manage(self):
        m = {}
        for i, num in enumerate(self.nums):
            l = m.get(num, None)
            if l:
                l.append(i)
            else:
                m[num] = [i]
        return m

    def pick(self, target):
        return random.choice(self.m[target])

    def pick1(self, target):
        """
        :type target: int
        :rtype: int
        """
        j = 1
        ret = -1
        i = 0
        while i < len(self.nums):
            if self.nums[i] == target:
                if random.randint(1, j) == j:
                    ret = i
                j += 1
            i += 1
        return ret





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
