# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = int((start + end) / 2)
        while start <= end:
            print(start, mid, end)
            guess_mid = guess(mid)
            if guess_mid == 0:
                return mid
            elif guess_mid == 1:
                start = mid + 1
                mid = int((start + end)) / 2
            else:
                end = mid - 1
                mid = int((start + end)) / 2
        print(start, mid, end)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
