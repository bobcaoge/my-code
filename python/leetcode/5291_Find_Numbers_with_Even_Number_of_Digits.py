# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([len(str(num)) % 2 == 0 for num in nums])


def main():
    s = Solution()


if __name__ == "__main__":
    main()
