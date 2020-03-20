# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = [["" for _ in range(3)] for __ in range(3)]
        flag = True
        for x, y in moves:
            grid[x][y] = "X" if flag else "O"
            flag = not flag
        def judge(target, grid):
            if [target]*3 in grid:
                return True
            for i in range(3):
                for j in range(3):
                    if grid[j][i] != target:
                        break
                else:
                    return True
            for i in range(3):
                if grid[i][i] != target:
                    break
            else:
                return True
            for i in range(3):
                if grid[i][2-i] != target:
                    break
            else:
                return True
            return False
        if judge('X', grid):
            return "A"
        if judge("O", grid):
            return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"



def main():
    s = Solution()
    print(s.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))


if __name__ == "__main__":
    main()
