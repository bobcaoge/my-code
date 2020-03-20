# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x, y = 0, 0
        for i in range(64):
            row = i/8
            column = i%8
            if board[row][column] == 'R':
                x, y = row, column
                break
        count = 0
        for i in range(y+1, 8):
            if board[x][i] == 'B':
                break
            if board[x][i] == 'p':
                count += 1
                break
        for i in range(y-1, -1, -1):
            if board[x][i] == 'B':
                break
            if board[x][i] == 'p':
                count += 1
                break
        for i in range(x+1, 8):
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                count += 1
                break
        for i in range(x-1, -1, -1):
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                count += 1
                break
        return count





def main():
    s = Solution()


if __name__ == "__main__":
    main()
