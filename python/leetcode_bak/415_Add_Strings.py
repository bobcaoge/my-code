# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def addStrings1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = ""
        length1 = len(num1)
        length2 = len(num2)
        if length1 < length2:
            short_s = num1
            long_s = num2
            length1 = length1
            length2 = length2
        else:
            short_s = num2
            long_s = num1
            length1 = length2
            length2 = length1
        i = 1
        carry = 0
        while i <= length1 or i <= length2:
            a = 0 if length1-i < 0 else int(short_s[length1-i])
            b = 0 if length2 -i < 0 else int(long_s[length2-i])
            buffer = a+b+ carry
            ret = str(int(buffer%10)) + ret
            carry = int(buffer/10)
            i+=1
        if carry:
            ret = str(carry)+ret
        return ret
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = ""
        length1 = len(num1)
        length2 = len(num2)
        i = 1
        carry = 0
        while i <= length1 or i <= length2:
            a = 0 if length1-i < 0 else int(num1[length1-i])
            b = 0 if length2 -i < 0 else int(num2[length2-i])
            buffer = a+b+ carry
            ret = str(int(buffer%10)) + ret
            carry = int(buffer/10)
            i+=1
        if carry:
            ret = str(carry)+ret
        return ret

def main():
    s = Solution()
    print(s.addStrings("1234567", "12"))


if __name__ == "__main__":
    main()
