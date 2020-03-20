# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def traverse(self, board, row, column, i, j):
            board[i][j] = "1"
            if 0 <= i-1 < row and 0 <= j < column and board[i-1][j] == "O":
                self.traverse(board, row, column, i-1, j)
            if 0 <= i+1 < row and 0 <= j < column and board[i+1][j] == "O":
                self.traverse(board, row, column, i+1, j)
            if 0 <= i < row and 0 <= j-1 < column and board[i][j-1] == "O":
                self.traverse(board, row, column, i, j-1)
            if 0 <= i < row and 0 <= j+1 < column and board[i][j+1] == "O":
                self.traverse(board, row, column, i, j+1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board:
            row = len(board)
            column = len(board[0])
            if row > 1 or column > 1:
                for i in range(row):
                    # scan from first column
                    if board[i][0] == "O":
                        self.traverse(board, row, column, i, 0)
                    # scan from last column
                    if board[i][column-1] == "O":
                        self.traverse(board, row, column, i, column-1)
                for j in range(column):
                    # scan from first row
                    if board[0][j] == "O":
                        self.traverse(board, row, column, 0, j)
                    # scan from last row
                    if board[row-1][j] == "O":
                        self.traverse(board, row, column, row-1, j)
                for i in range(row):
                    for j in range(column):
                        if board[i][j] == "1":
                            board[i][j] = "O"
                        elif board[i][j] == "O":
                            board[i][j] = "X"


def main():
    s = Solution()
    s.solve([])


if __name__ == "__main__":
    main()
