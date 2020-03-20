# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        ret = 0
        for i in range(len(matrix)):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                ret += 1

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 1:
                dp[0][i] = 1
                ret += 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])
                    if matrix[i-dp[i][j]][j-dp[i][j]] == 1:
                        dp[i][j] += 1
        return sum([sum(row) for row in dp])


def main():
    s = Solution()
    print(s.countSquares([
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]))


if __name__ == "__main__":
    main()
