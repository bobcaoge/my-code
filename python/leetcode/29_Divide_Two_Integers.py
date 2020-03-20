# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        minus = False
        if divisor < 0 < dividend or dividend < 0 < divisor :
            minus = True
        dividend = -dividend if dividend < 0 else dividend
        divisor = -divisor if divisor < 0 else divisor
        plus = 1
        ret = 0
        flag = divisor
        while dividend >= flag and divisor >= flag:
            if dividend - divisor >= 0:
                dividend -= divisor
                ret += plus
                divisor += divisor
                plus <<= 1
            else:
                divisor >>= 1
                plus >>= 1
        # print(dividend, divisor)
        if ret == 2147483648 and not minus:
            ret = 2147483647
        return ret if not minus else -ret



def main():
    s = Solution()
    print(s.divide(2**31, 1))

if __name__ == "__main__":
    main()
