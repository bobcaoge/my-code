# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n += 1
        ret = [0]*(n+1)
        ret[0] = 0
        ret[1] = 1
        ret[2] = 1
        if n == 2:
            return 1
        for i in range(3, n+1):
            for j in range(1, i):
                ret[i] = max(ret[j]*(i-j), ret[i], j*(i-j))
            print(ret)
        return ret[-1]



def main():
    s = Solution()
    print(s.integerBreak(4))
    print(s.integerBreak(20))
    print(s.integerBreak(58))


if __name__ == "__main__":
    main()
