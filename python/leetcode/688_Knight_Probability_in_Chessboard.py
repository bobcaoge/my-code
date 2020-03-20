# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[0]*N for _ in range(N)]
        dp[r][c] = 1
        num_out_of_chessboard = 0
        for i in range(K):
            dp = self.move(dp)
        return self.get_the_num_of_knight_in_chessboard(dp)

    def print_chessboard(self, chessboard):
        for row in chessboard:
            print(row)
        print("######################################")


    def get_the_num_of_knight_in_chessboard(self, chessboard):
        N = len(chessboard)
        num = 0
        for i in range(N):
            for j in range(N):
                num += chessboard[i][j]
        return num

    def move(self, chessboard):
        N = len(chessboard)
        buff_chessboard = [[0]*N for _ in range(N)]
        num_out_of_chessboard = 0
        for i in range(N):
            for j in range(N):
                if chessboard[i][j] > 0:
                    chessboard[i][j] *= 1/8.0
                    # move in eight directions
                    for dr, dc in [(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]:
                        if 0 <= i+dr < N and 0<= j+dc < N:
                            buff_chessboard[i+dr][j+dc] += chessboard[i][j]
        return buff_chessboard


def main():
    s = Solution()
    print(s.knightProbability(3,2,0,0))


if __name__ == "__main__":
    main()
