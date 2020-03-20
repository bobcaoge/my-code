# /usr/bin/python3.6
# -*- coding:utf-8 -*-

import queue

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # 去掉所有子数组中仅包含小于 L 的数组
        ret = 0
        start = -1
        length_lt_L = 0
        A.append(R+1)
        for i, num in enumerate(A):
            if num >= L:
                ret -= length_lt_L*(length_lt_L+1)/2
                length_lt_L = 0
                if num >R:
                    length = i - start-1
                    start = i
                    ret += length*(length+1)/2
            else:
                length_lt_L += 1
        return ret


def main():
    s = Solution()
    print(s.numSubarrayBoundedMax([2,1,4,3], 2, 3))
    print(s.numSubarrayBoundedMax([2,1,4,3,1,2,1,2,1,2,1,2,1,2,2,2,2,2,2,2,4,4,4,4], 2, 3))
    print(s.numSubarrayBoundedMax([16,69,88,85,79,87,37,33,39,34],55,57))


if __name__ == "__main__":
    main()
