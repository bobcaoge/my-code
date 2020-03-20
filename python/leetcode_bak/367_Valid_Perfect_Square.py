# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 方法一， 从0遍历， 分奇偶
        # i = 0 if num %2 == 0 else 1
        # while i <= num:
        #     if i ** 2 == num:
        #         return True
        #     if i**2 > num:
        #         return False
        #     i+=2
        # 方法二， 用内建函数， 开方
        # square = num**0.5
        # return square == int(square)
        # 方法三， 二分法查找
        if num == 1 or num == 1:
            return True
        start = 0
        end = num - 1
        mid = int(end / 2)
        while start != mid:
            if mid * mid == num:
                return True
            if mid * mid > num:
                end = mid
                mid = int((start + end) / 2)
            else:
                start = mid
                mid = int((start + end) / 2)
        return False


def main():
    s = Solution()


if __name__ == "__main__":
    main()
