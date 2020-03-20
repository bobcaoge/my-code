# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def analysis(self, s, positive):
        num = 0
        num_of_x = 0
        start = 0
        for index, c in enumerate(s):
            if c in {'-', '+'}:
                if 'x' not in s[start:index]:
                    cur = int(s[start:index])
                    num += cur if positive else -cur
                else:
                    if s[start:index] == 'x':
                        cur = 1
                    else:
                        cur = int(s[start:index-1])
                    num_of_x += cur if positive else -cur
                positive = (c == '+')
                start = index+1
        return num, num_of_x
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        eq = equation.split("=")
        eq[0] += '+'
        eq[1] += '+'
        if eq[0][0] == '-':
            eq[0] = '0'+eq[0]
        if eq[1][0] == '-':
            eq[1] = '0'+eq[1]



        num, num_of_x = self.analysis(eq[0], True)
        res = self.analysis(eq[1], True)
        num -= res[0]
        num_of_x -= res[1]

        if num_of_x == 0:
            if num == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:

            return "x={0}".format(-num/num_of_x)


def main():
    s = Solution()
    print(s.solveEquation("x+5-3+x=6+x-2"))
    print(s.solveEquation("x=-2"))
    print(s.solveEquation("2x=4"))
    print(s.solveEquation("x+1=x+1"))
    print(s.solveEquation("x=x+1"))


if __name__ == "__main__":
    main()
