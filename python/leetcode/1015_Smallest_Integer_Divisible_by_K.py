# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K == 1:
            return 1
        length = 0
        cur = 0
        old = set()
        while True:
            length += 1
            cur = (cur*10%K + 1 % K)%K
            if cur == 0:
                return length
            if cur in old:
                return -1
            old.add(cur)


def main():
    s = Solution()
    print(s.smallestRepunitDivByK(2))
    print(s.smallestRepunitDivByK(3))
    print(s.smallestRepunitDivByK(4441))


if __name__ == "__main__":
    main()
