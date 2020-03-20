# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isvalid_of_row_and_column(board, i):
            row = set()
            column = set()
            for j in range(9):
                a = board[i][j]
                if a != ".":
                    if a in row:
                        return False
                    row.add(a)
                b = board[j][i]
                if b != ".":
                    if b in column:
                        return False
                    column.add(b)
            return True

        def isvalid_of_block(board, x, y):
            s = set()
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    cur = board[i][j]
                    if cur != ".":
                        if cur in s:
                            return False
                        s.add(cur)
            return True
        row_and_column = [1,4,7]
        for i in row_and_column:
            for j in row_and_column:
                if not isvalid_of_block(board, i, j):
                    return False
        for i in range(9):
            if not isvalid_of_row_and_column(board, i):
                return False
        return True


def main():
    s = Solution()


if __name__ == "__main__":
    main()
