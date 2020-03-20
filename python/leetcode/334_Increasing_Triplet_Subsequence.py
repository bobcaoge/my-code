# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        first = second = 2**32
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False




def main():
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))
    print(s.increasingTriplet([1,2,3,4,5][::-1]))
    print(s.increasingTriplet([1,0,2,0,3,0,4,0]))
    print(s.increasingTriplet([1,2,-10,-8,-7]))


if __name__ == "__main__":
    main()
