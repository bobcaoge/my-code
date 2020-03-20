# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        cur = 0
        for num in nums:

            if num == 1:
                cur += 1
            else:
                ret = max(ret, cur)
                cur = 0

        return max(ret, cur)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
