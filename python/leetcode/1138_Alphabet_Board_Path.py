# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        m = {}
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                m[c] = (i, j)

        x, y = 0, 0
        ret = ""
        for c in target:
            xx, yy = m[c]
            if (x, y) == (xx, yy):
                ret += "!"
            else:
                dx = xx - x
                dy = yy - y

                abs_dx = abs(dx)
                abs_dy = abs(dy)
                if dx >= 0 and dy >= 0:
                    ret += "R"*abs_dy+"D"*abs_dx
                elif dx >= 0 and dy <= 0:
                    ret += "L"*abs_dy+"D"*abs_dx
                elif dx <= 0 and dy <= 0:
                    ret += "L"*abs_dy+"U"*abs_dx
                else:
                    ret += "U"*abs_dx+"R"*abs_dy
                ret += "!"
            x, y = xx, yy
        return ret


def main():
    s = Solution()
    print(s.alphabetBoardPath("leet"))
    print(s.alphabetBoardPath("code"))


if __name__ == "__main__":
    main()
