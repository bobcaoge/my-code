# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits1(self, n):
        ret = 0
        for i in range(32):
            ret = ret * 2 + n%2
            print(n%2, end="")
            n = int(n/2)
        return ret
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            ret = ret << 1
            if n & 1 == 1:
                ret += 1
            n = n >> 1
        return ret


def main():
    s = Solution()
    print( s.reverseBits(5))


if __name__ == "__main__":
    main()
