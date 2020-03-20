# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        length = len(nums)
        for num in nums:
            m[num] = m.get(num, 0) + 1
        ret = []
        for i in range(1, length+1):
            buffer = m.get(i, 0)
            if buffer == 2:
                ret.insert(0, i)
            if buffer == 0:
                ret.append(i)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
