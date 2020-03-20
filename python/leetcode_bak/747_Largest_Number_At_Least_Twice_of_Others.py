# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -2 ** 23
        index_of_max_num = -1
        for index, num in enumerate(nums):
            if num > max_num:
                max_num = num
                index_of_max_num = index
        for num in nums:
            if num != max_num and max_num < 2 * num:
                return -1
        return index_of_max_num


def main():
    s = Solution()


if __name__ == "__main__":
    main()
