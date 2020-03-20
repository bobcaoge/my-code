# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = [0]*N
        ret = [0]
        def dfs(x):
            if x == N+1:
                ret[0] += 1
                return
            for i in range(1, N+1):
                if num[i-1] == 0 and (i % x == 0 or x % i == 0):
                    num[i-1] = x
                    dfs(x+1)
                    num[i-1] = 0
        dfs(1)
        return ret[0]



def main():
    s = Solution()
    print(s.countArrangement(15))


if __name__ == "__main__":
    main()
