# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        ret = 1
        i = 2
        while i**2 <= n:
            ret += 1
            i += 1
        return ret


def main():
    s = Solution()
    print(s.bulbSwitch(3))
    print(s.bulbSwitch(4))
    print(s.bulbSwitch(10))
    print(s.bulbSwitch(9999999))


if __name__ == "__main__":
    main()
