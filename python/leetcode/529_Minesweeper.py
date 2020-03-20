# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        row = len(board)
        column = len(board[0])

        def count(x, y):
            ret = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0<=x+dx<row and 0<=y+dy<column and board[x+dx][y+dy] == "M":
                        ret += 1
            return ret

        def dfs(x, y):
            if board[x][y] != "E":
                return
            num = count(x, y)
            if num > 0:
                board[x][y] = str(num)
            else:
                board[x][y] = 'B'
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= x+dx < row and 0 <= y+dy < column:
                            dfs(x+dx, y+dy)
        dfs(x, y)
        return board



def main():
    s = Solution()
    print(s.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
                        ,[3,0]))


if __name__ == "__main__":
    main()
