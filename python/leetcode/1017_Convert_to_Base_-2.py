# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        for i in range(1, 33, 2):
            if ((N >> i) & 1) == 1:
                N += (1 << (i+1))
        return bin(N)[2:]


def main():
    s = Solution()
    print(s.baseNeg2(7))
    print(s.baseNeg2(3))


if __name__ == "__main__":
    main()
