# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def solve():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for c in "123456789":
                            if is_valid(i, j, c):
                                board[i][j] = c
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        def is_valid(i, j, c):
            for k in range(9):
                if board[k][j] == c and k != i:
                    return False
                if board[i][k] == c and k != j:
                    return False
                if board[i//3*3+k//3][j//3*3+k%3] == c:
                    return False
            return True
        solve()



def main():
    s = Solution()


if __name__ == "__main__":
    main()
