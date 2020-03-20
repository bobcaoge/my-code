# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    def div(self, a, b):
        while a % b != 0:
            a, b = b, a % b
        return b

    def addition(self, first_frac, second_frac, flag):
        a, b = first_frac
        c, d = second_frac
        numerator = a*d + b*c if flag else a*d-b*c
        denominator = b*d
        if numerator == 0:
            return [0,1]
        common_divisor = self.div(numerator, denominator)
        return numerator/common_divisor, denominator/common_divisor

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        signs = []
        start = 0
        if expression[0] != '-':
            signs.append("+")
        else:
            start = 1
            signs.append("-")
        nums = []
        old = start
        for i in range(start, len(expression)):
            if expression[i] in {"/", "+", "-"}:
                if expression[i] in {"+", "-"}:
                    signs.append(expression[i])
                nums.append(int(expression[old:i]))
                old = i+1
        nums.append(int(expression[old:]))
        print(nums, signs)
        ret = [0, 1]
        for i, c in enumerate(signs):
            ret = self.addition(ret, nums[i*2:i*2+2], c == "+")
        return "{0}/{1}".format(ret[0], ret[1])







def main():
    s = Solution()
    print(s.fractionAddition("-1/2+1/2+1/3"))


if __name__ == "__main__":
    main()
