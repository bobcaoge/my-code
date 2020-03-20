# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import copy


class Solution(object):
    flag = False
    board = [[]]
    row = 0
    column = 0

    def check1(self, s, word, x, y):
        # print(s)
        if not word or self.flag:
            self.flag = True
            return
        if 0 <= x-1 < self.row and 0 <= y < self.column:
            if self.board[x-1][y] == word[0] and (x-1, y) not in s:
                self.check1(s | {(x-1, y)}, word[1:], x-1, y)
        if 0 <= x+1 < self.row and 0 <= y < self.column:
            if self.board[x+1][y] == word[0] and (x+1, y) not in s:
                self.check1(s | {(x+1, y)}, word[1:], x+1, y)
        if 0 <= x < self.row and 0 <= y-1 < self.column:
            if self.board[x][y-1] == word[0] and (x, y-1) not in s:
                self.check1(s | {(x, y-1)}, word[1:], x, y-1)
        if 0 <= x < self.row and 0 <= y+1 < self.column:
            if self.board[x][y+1] == word[0] and (x, y+1) not in s:
                self.check1(s | {(x, y+1)}, word[1:], x, y+1)

    def exist1(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True

        self.flag = False
        self.board = board
        row = len(board)
        self.row = row
        column = len(board[0])
        self.column = column
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0]:
                    self.check1({(i, j)}, word[1:], i, j)
        return self.flag

    def check(self, board, word, x, y):
        # print(s)
        if not word or self.flag:
            self.flag = True
            return
        if 0 <= x-1 < self.row and 0 <= y < self.column:
            if board[x-1][y] == word[0]:
                board[x-1][y] = "*"
                self.check(board, word[1:], x-1, y)
                board[x-1][y] = word[0]
        if 0 <= x+1 < self.row and 0 <= y < self.column:
            if board[x+1][y] == word[0]:
                board[x+1][y] = "*"
                self.check(board, word[1:], x+1, y)
                board[x+1][y] =word[0]
        if 0 <= x < self.row and 0 <= y-1 < self.column:
            if board[x][y-1] == word[0]:
                board[x][y-1] = "*"
                self.check(board, word[1:], x, y-1)
                board[x][y-1] = word[0]
        if 0 <= x < self.row and 0 <= y+1 < self.column:
            if board[x][y+1] == word[0]:
                board[x][y+1] = "*"
                self.check(board, word[1:], x, y+1)
                board[x][y+1] = word[0]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        self.flag = False
        self.board = board
        row = len(board)
        self.row = row
        column = len(board[0])
        self.column = column
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0]:
                    board[i][j] = "*"
                    self.check(board, word[1:], i, j)
                    board[i][j] = word[0]
        return self.flag


def main():
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print(s.exist([["a","a"]], "aaa"))
    print(s.exist([["a","a"]], "a"))


if __name__ == "__main__":
    main()
