# /usr/bin/python3.6
# -*- coding:utf-8 -*-

import re
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        pattern = re.compile(r"-?\d+")
        for op in ops:
            print(points)
            if pattern.findall(op):
                points.append(int(op))
            elif op == "C":
                points.pop()
            elif op == "D":
                points.append(points[-1]*2)
            elif op == "+":
                points.append(points[-1]+points[-2])
        return sum(points)


def main():
    s = Solution()
    print(s.calPoints(["-21","-66","39","+","+"]))

if __name__ == "__main__":
    main()
