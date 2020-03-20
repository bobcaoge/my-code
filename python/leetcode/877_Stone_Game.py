# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        f = [[0]*len(piles) for _ in range(len(piles))]
        s = [[0]*len(piles) for _ in range(len(piles))]
        for i in range(len(piles)-1, -1, -1):
            f[i][i] = piles[i]
            for j in range(i+1, len(piles)):
                f[i][j] = max(s[i+1][j]+piles[i], s[i][j-1]+piles[j])
                s[i][j] = min(f[i+1][j], f[i][j-1])
        return f[0][-1] > s[0][-1]


def main():
    s = Solution()
    print(s.stoneGame([5,3,4,5]))
    print(s.stoneGame([1,2,4,6,8,3,6,7,4,5,3,2,5,7,8,4,3,6,7,5,4,3,2,5]))


if __name__ == "__main__":
    main()
