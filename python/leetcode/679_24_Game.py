# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import itertools


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return abs(nums[0] - 24) < 0.0001
        for x in itertools.permutations(nums):
            x = list(x)
            a, b = x[:2]
            for y in (a*b, a-b, a+b):
                if self.judgePoint24(x[2:] +[y]):
                    return True
            if b != 0:
                if self.judgePoint24(x[2:]+[a/b]):
                    return True
        return False




def main():
    s = Solution()
    print(s.judgePoint24([8,7,1,4]))
    print(s.judgePoint24([5,5,8,4]))
    print(s.judgePoint24([1,2,1,2]))
    print(s.judgePoint24([1,3,4,6]))


if __name__ == "__main__":
    main()
