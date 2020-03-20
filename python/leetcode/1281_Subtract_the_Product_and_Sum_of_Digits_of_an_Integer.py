# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from functools import reduce

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        return reduce(lambda x, y: x*y, [int(c) for c in str(n)]) - reduce(lambda x, y: x+y, [int(c) for c in str(n)])


def main():
    s = Solution()
    print(s.subtractProductAndSum(234))


if __name__ == "__main__":
    main()
