# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def changged(self, board, x, y, row, column):
        count_of_zeros = 0
        count_of_ones = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0<= i < row and 0<= j < column:
                    if board[i][j] == 0 or board[i][j] == 2:
                        count_of_zeros += 1
                    else:
                        count_of_ones += 1
        if board[x][y] == 0:
            if count_of_ones == 3:
                return 2
            else:
                return 0
        if board[x][y] == 1:
            if 3 <= count_of_ones <= 4:
                return 1
            else:
                return 3

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                board[i][j] = self.changged(board, i, j, row, column)
        print(board)
        for i in range(row):
            for j in range(column):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        print(board)



def main():
    s = Solution()
    print(s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))


if __name__ == "__main__":
    main()
