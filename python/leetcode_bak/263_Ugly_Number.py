# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def primes(self, n):
        table = [True] * n
        table[0] = table[1] = False
        for i in range(2,int(n**0.5)+1):
            table[i*i:n:i] = [False]*len(table[i*i::i])
        return [index for index, value in enumerate(table) if value is True]

    def isUgly1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = abs(num)
        while num %2 == 0:
            num = int(num/2)
        print(num)
        if num < 7:
            return True
        primes_list = self.primes(num+1)
        for i in range(3, len(primes_list)):
            if num%primes_list[i] == 0:
                return False
        return True
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num %2 == 0:
            num = int(num/2)
        while num %3 == 0:
            num = int(num/3)
        while num %5 == 0:
            num = int(num/5)
        if num != 1:
            return False
        return True


def main():
    s = Solution()
    # print(s.primes(14))
    # print(s.isUgly(14))
    print(s.isUgly(-2147483648))


if __name__ == "__main__":
    main()
