# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n == 1:
            return 1
        m -= 1
        n -= 1
        if m< n:
            m = m+n
            n = m-n
            m = m-n
        res = 1
        j = 1
        for i in range(m+1, m+n+1):
            res *= i
            res /= j
            j += 1
        return res




    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        else:
            ret = 0
            for i in range(1, n):
                ret += self.uniquePaths(m-1, n-i)
            for j in range(1, m):
                ret += self.uniquePaths(m-j, n-1)
            return ret


def main():
    s = Solution()
    print(s.uniquePaths(3,2))

if __name__ == "__main__":
    main()
