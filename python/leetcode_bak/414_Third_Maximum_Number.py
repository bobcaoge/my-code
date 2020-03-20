# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -2**32
        second = -2**32
        third = -2**32
        for num in nums:
            if num > max_num:
                third = second
                second = max_num
                max_num = num
            elif max_num > num > second :
                third = second
                second = num
            elif second > num > third:
                third = num
        if third != -2**32:
            return third
        else:
            return max_num


def main():
    s = Solution()
    print(s.thirdMax([2,2,3,1]))


if __name__ == "__main__":
    main()
