# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        length = len(num1)+len(num2) - 1
        ret = [0]*length
        for i, num_i in enumerate(num1):
            for j, num_j in enumerate(num2):
                ret[i+j] += int(num_i)*int(num_j)
        carry = 0
        for i in range(length-1, -1, -1):
            cur = ret[i] + carry
            ret[i] = str(cur % 10)
            carry = int(cur / 10)

        if carry == 0:
            return "".join(ret)
        else:
            return str(carry) + "".join(ret)

    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        length = len(num1)+len(num2) - 1
        ret = [0]*length
        for i, num_i in enumerate(num1):
            for j, num_j in enumerate(num2):
                ret[i+j] += int(num_i)*int(num_j)
        carry = 0
        for i in range(length-1, -1, -1):
            cur = ret[i] + carry
            ret[i] = cur % 10
            carry = int(cur / 10)
        # print(ret)

        if carry == 0:
            return "".join([str(num) for num in ret])
        else:
            return str(carry) + "".join([str(num) for num in ret])


def main():
    s = Solution()
    print(s.multiply("22", "23"))
    print(s.multiply("99", "99"))
    print(s.multiply("0", "99"))


if __name__ == "__main__":
    main()
