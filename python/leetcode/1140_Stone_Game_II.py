# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        memo = {}
        def dfs(i, alex_turn, m):
            if i >= len(piles):
                return 0
            if memo.get((i,alex_turn, m), -1) == -1:
                ret = 0
                if alex_turn:
                    for j in range(1, min(2*m+1, len(piles))):
                        ret = max(ret, sum(piles[i:i+j])+dfs(i+j, not alex_turn, max(m, j)))
                else:
                    ret = 1<<31
                    for j in range(1, min(2*m+1, len(piles))):
                        ret = min(ret, dfs(i+j, not alex_turn, max(m, j)))
                memo[(i, alex_turn, m)] = ret
            return memo[(i, alex_turn, m)]
        return dfs(0, True, 1)



def main():
    s = Solution()
    print(s.stoneGameII([2,7,9,4,4]))
    print(s.stoneGameII([1,2,3,4,5,3,1,3,5,3,2,4,5,3,2,3,5,7,7,8,6,5,4,3,4,5,6]))


if __name__ == "__main__":
    main()
