# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import functools
# 此代码 Python2 运行通过 Python3失败

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        dp = [[0 for __ in range(3)] for _ in range(len(stoneValue))]
        for i in range(len(stoneValue)-1, -1, -1):
            cur_sum = 0
            for j in range(3):
                cur_sum += stoneValue[i+j] if i+j < len(stoneValue) else 0
                dp[i][j] = cur_sum + min([min(dp[i+j+x]) if i+j+x <len(stoneValue) else 0 for x in range(2, 5)])
        score_of_Alice = max(dp[0])
        score_of_bob = sum(stoneValue)-score_of_Alice
        if score_of_Alice > score_of_bob:
            return "Alice"
        if score_of_Alice == score_of_bob:
            return "Tie"
        return "Bob"
    def stoneGameIII_1(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        memo = {}
        @functools.lru_cache(None)
        def get(i, score_of_alice, score_of_bob, flag):
            if memo.get((score_of_alice, score_of_bob, flag, i), -1000) == -1000:

                if i >= len(stoneValue):
                    return 1 if score_of_alice > score_of_bob else 0 if score_of_alice == score_of_bob else -1
                ret = -1 if flag else 1
                for j in range(i, min(3+i, len(stoneValue))):
                    res = get(j+1,
                           score_of_alice+(sum(stoneValue[i:j+1]) if flag else 0),
                           score_of_bob+(sum(stoneValue[i:j+1]) if not flag else 0),
                           not flag)
                    if flag:
                        ret = max(ret, res)
                        if res == 1:
                            break
                    if not flag:
                        ret = min(ret, res)
                        if res == -1:
                            break

                memo[(score_of_alice, score_of_bob, flag, i)] = ret
            return memo[(score_of_alice, score_of_bob, flag, i)]
        m = {1:"Alice",
             0:"Tie",
             -1:"Bob"}
        flag = get(0, 0, 0, True)
        return m[flag]


def main():
    s = Solution()
    print(s.stoneGameIII([1,2,3,-9]))


if __name__ == "__main__":
    main()
