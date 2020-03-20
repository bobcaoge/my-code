# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        index = -1
        length_a = len(a)
        length_b = len(b)
        rer_s = ["" for x in range(0, max(length_a, length_b))]

        carry = 0
        while index >= -min(len(a), len(b)):
            buffer = int(a[index]) + int(b[index])+carry
            rer_s[index] = str(buffer%2)
            carry = int(buffer/2)
            index -= 1

        while index >= -len(a):
            buffer = int(a[index])+carry
            rer_s[index] = str(buffer%2)
            carry = int(buffer/2)
            index -= 1

        while index >= -len(b):
            buffer = int(b[index])+carry
            rer_s[index] = str(buffer%2)
            carry = int(buffer/2)
            index -= 1

        if carry > 0:
             return str(carry) + "".join(rer_s)

        return  "".join(rer_s)



def main():
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))


if __name__ == "__main__":
    main()
