# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def judgeCircle1(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        m = {
            "U": 0,
            "D": 0,
            "L": 0,
            "R": 0
        }
        for move in moves:
            m[move] += 1

        return m["U"] == m["D"] and m["L"] == m["R"]

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up_and_down = 0
        left_and_right = 0
        for move in moves:
            if move == "U":
                up_and_down += 1
            elif move == "D":
                up_and_down -= 1
            elif move == "L":
                left_and_right += 1
            elif move == "R":
                left_and_right -= 1
        if up_and_down == left_and_right == 0:
            return True
        return False


def main():
    s = Solution()


if __name__ == "__main__":
    main()
