# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):

    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        m = collections.Counter(A)
        nums = sorted(set(A))
        ret = 0
        mod = 10**9+7
        for i, num in enumerate(nums):
            # 三个数全不相等
            for j in range(i+1, len(nums)):
                third = target - num - nums[j]
                if third > nums[j]:
                    ret += m[num]*m[nums[j]]*m.get(third, 0) % mod
            # 有两个数相等
            third = target - num*2
            if third != num:
                nums_of_third = m.get(third, 0)
                nums_of_first = m[num]
                ret += (nums_of_first-1)*nums_of_first / 2*nums_of_third
            # 有三个数相等
            if num*3 == target:
                nums_of_first = m[num]
                ret += (nums_of_first-1)*nums_of_first*(nums_of_first-2)/6%mod
        return ret


def main():
    s = Solution()
    print(s.threeSumMulti(A = [1,1,2,2,3,3,4,4,5,5], target = 8))
    print(s.threeSumMulti(A = [1,1,2,2,2,2], target = 5))
    print(s.threeSumMulti(A = [2,2,2,2,2,2], target = 6))


if __name__ == "__main__":
    main()
