# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        N, R = divmod(N, 25)
        N = N + (R > 0)
        memo = {}
        def dp(x, y):
            if memo.get((x,y), -1) == -1:
                ans = 0
                if x <= 0 and y <= 0:
                    ans = 0.5
                elif x <= 0 and y > 0:
                    ans = 1
                elif x > 0 and y <= 0:
                    ans = 0
                else:
                    ans = 0.25*(dp(x-4, y)+dp(x-3, y-1)+dp(x-2, y-2)+dp(x-1, y-3))
                memo[(x, y)] = ans
            return memo[(x, y)]
        return dp(N, N)




def main():
    s = Solution()
    print(s.soupServings(1000))


if __name__ == "__main__":
    main()
