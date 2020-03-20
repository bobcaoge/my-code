# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        buff = []
        ret = []
        for i in range(len(nums)-1, -1, -1):
            pos = bisect.bisect(buff, nums[i]-1)
            ret.append(pos)
            buff.insert(pos, nums[i])
        return ret[::-1]


def main():
    s = Solution()
    print(s.countSmaller([5,4,3,2,1]))
    print(s.countSmaller([5,3,2,1,4]))


if __name__ == "__main__":
    main()
