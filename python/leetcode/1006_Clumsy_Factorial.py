# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        m = {
            1: 1,
            2: 2,
            3: 6
        }
        if N <= 3:
            return m[N]
        ret = N*(N-1)//(N-2)+(N-3)
        N -= 4
        while N >= 4:
            ret = ret - N*(N-1)//(N-2)+(N-3)
            N -= 4
        if 0< N <= 3:
            ret -= m[N]
        return ret


def main():
    s = Solution()
    print(s.clumsy(4))
    print(s.clumsy(10))


if __name__ == "__main__":
    main()
