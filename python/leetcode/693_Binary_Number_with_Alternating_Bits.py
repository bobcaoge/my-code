# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cur = n % 2
        while n != 0:
            if cur != n % 2:
                return False
            cur += 1
            cur %= 2
            n = int(n/2)
        return True


def main():
    s = Solution()
    print(s.hasAlternatingBits(5))
    print(s.hasAlternatingBits(7))
    print(s.hasAlternatingBits(11))
    print(s.hasAlternatingBits(10))


if __name__ == "__main__":
    main()
