# /usr/bin/python3.6
# -*- coding:utf-8 -*-

import copy
class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = {}
        keys = set()
        for num in nums:
            m[num] = m.get(num, 0) + 1
            keys.add(num)
        ret = []
        for k in keys:
            m[k] -= 1
            s = set()
            for key, value in m.items():
                if value == 0:
                    continue
                if key in s:
                    continue
                m[key] -= 1
                if m.get(-k-key, 0) != 0:
                    ret.append([k, key, -k-key])
                    s.add(-k-key)
                m[key] += 1
            m[k] = 0
        return ret




def main():
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 0, 0, 0]))
    print(s.threeSum([-2, 0, 0, 2, 2]))
    print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
    print(s.threeSum([0, 0]))


if __name__ == "__main__":
    main()
