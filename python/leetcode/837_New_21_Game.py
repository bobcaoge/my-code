# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0:
            return 1.0
        dp = [0]*(N+1)
        dp[0] = 1

        wsum = 1
        res = 0
        for i in range(1, N+1):
            dp[i] = wsum / W
            if i>=W:
                wsum -= dp[i-W]
            if i < K:
                wsum += dp[i]
            else:
                res += dp[i]
        return res


    def new21Game1(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if N >= K*W:
            return 1
        dp = [[0.0]*(K+W) for _ in range(K+1)]
        dp[0][0] = 1
        p_base = 1.0/W
        ret = 0.0
        for i in range(1, K+1):
            for j in range(1, K+W):
                if i*W < j:
                    break
                for w in range(1, W+1):
                    if K > j-w >= 0:
                        dp[i][j] += dp[i-1][j-w]*p_base
                    # if j-W < 0:
                    #     break

                if N >= j >= K:
                    ret += dp[i][j]
        return ret


def main():
    s = Solution()
    print(s.new21Game(10, 1, 10))
    print(s.new21Game(21, 17, 10))
    print(s.new21Game(1000, 1000, 10))


if __name__ == "__main__":
    main()
