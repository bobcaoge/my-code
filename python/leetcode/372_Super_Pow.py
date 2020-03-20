# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    base = 1337

    def f(self, a, b):
        """
        calculate a^b/1337  0<= b < 10
        :param a:
        :param b:
        :return:
        """
        a %= self.base
        result = 0
        for i in range(b):
            result = (result*a)%self.base
        return result

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        last_digit = b.pop()
        return self.f(self.superPow(a, b), 10) * self.f(a, last_digit)%self.base

    def superPow1(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        p = 0
        for num in b:
            p = (p*10+num) % 1140
        if p == 0:
            p += 1140
        return self.f(a, p)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
