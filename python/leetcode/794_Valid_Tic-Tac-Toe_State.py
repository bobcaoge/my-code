# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        # 判断是否有赢家
        m = {
            "X": False,
            "O": False
        }

        x = 0
        o = 0
        for i in range(3):
            x += board[i].count("X")
            o += board[i].count("O")
        if x - o > 1:
            return False

        if "XXX" in board:
            m['X'] = True
        if "OOO" in board:
            m['O'] = True

        for i in range(3):
            if [board[j][i] for j in range(3)] in [['X', 'X', 'X'], ['O', 'O', 'O']]:
                m[board[0][i]] = True

        if board[0][0] ==  board[2][2] == board[1][1] == "X":
            m['X'] = True
        if board[0][0] ==  board[2][2] == board[1][1] == "O":
            m['O'] = True

        if board[0][2] ==  board[2][0] == board[1][1] == "X":
            m['X'] = True
        if board[0][2] ==  board[2][0] == board[1][1] == "O":
            m['O'] = True

        if m['X'] and m['O']:
            return False
        elif m['X']:
            if x - o == 1:
                return True
        elif m['O']:
            if o - x == 0:
                return True
        else:
            if x - o in {0, 1}:
                return True
        return  False



def main():
    s = Solution()
    print(s.validTicTacToe(["O  ","   ","   "]))
    print(s.validTicTacToe(["XOX", "O O", "XOX"]))
    print(s.validTicTacToe(["XXX", "   ", "O O"]))
    print(s.validTicTacToe(["XOX", " X ", "   "]))
    print(s.validTicTacToe(["XXX","OOX","OOX"]))


if __name__ == "__main__":
    main()
