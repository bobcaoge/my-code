# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_of_nums = sum(nums)
        cur = 0
        for index, num in enumerate(nums):
            if sum_of_nums - cur - num == cur:
                return index
            cur += num
        return -1




def main():
    s = Solution()


if __name__ == "__main__":
    main()
