# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        ret = ""
        movement_before = "L"
        old_pos = -1
        for i, c in enumerate(dominoes+"R"):
            if c == "L":
                if movement_before == "L":
                    ret += "L"*(i-old_pos)
                if movement_before == "R":
                    num = i-old_pos+1
                    half = int(num / 2)
                    if num % 2 == 0:
                        ret += "R"*half + "L"*(half-1)
                    if num % 2 == 1:
                        ret += "R"*half+"." + "L"*(half-1)
                movement_before = "L"
                old_pos = i
            if c == "R":
                if movement_before == "L":
                    ret += "L" + "."*(i-old_pos-1)
                if movement_before == "R":
                    ret += "R"*(i-old_pos)
                movement_before = c
                old_pos = i
        return ret[1:]


def main():
    s = Solution()
    print(s.pushDominoes(".L.R...LR..L.."))
    print(s.pushDominoes("RR.L"))
    print(s.pushDominoes(".....RRRR.....LLLLRRRRLLLL......RRRRR....."))


if __name__ == "__main__":
    main()
