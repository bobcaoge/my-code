# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 1:
            return 1
        self.ret = 0
        memo = {}

        def dfs(i): # 第i个位置被占用
            if memo.get(i, -1) == -1:
                if i == n-2:
                    return 1
                else:
                    ret = 0
                    for j in range(i+1, n):
                        ret += dfs(j)*(1.0/(n-i-1))
                    memo[i] = ret
            return memo[i]

        for i in range(n):
            self.ret += dfs(i)*(1.0/n)
        return self.ret

def main():
    s = Solution()
    print(s.nthPersonGetsNthSeat(1))
    print(s.nthPersonGetsNthSeat(2))
    print(s.nthPersonGetsNthSeat(100))


if __name__ == "__main__":
    main()
