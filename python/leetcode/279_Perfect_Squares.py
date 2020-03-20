# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        keep = [n] * (n+1)
        keep[0] = 0
        for i in range(1, n+1):
            square = int(n**0.5)
            if square**2 == n:
                keep[i] = 1
            for j in range(1, square+1):
                keep[i] = min(keep[i], keep[i-j*j]+1)
        return keep[-1]


def main():
    s = Solution()
    print(s.numSquares(12))
    print(s.numSquares(13))
    print(s.numSquares(999))
    print(s.numSquares(3))
    print(s.numSquares(48))


if __name__ == "__main__":
    main()
