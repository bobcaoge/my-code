# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:
            return False
        m = collections.Counter(nums)
        arr = sorted(set(nums))
        for num in arr:
            if m[num] > 0:
                number = m[num]
                for i in range(k):
                    m[num+i] -= number
        return all([x == 0 for _, x in m.items()])


def main():
    s = Solution()
    print(s.isPossibleDivide(nums = [1,2,3,3,4,4,5,9], k = 4))


if __name__ == "__main__":
    main()
