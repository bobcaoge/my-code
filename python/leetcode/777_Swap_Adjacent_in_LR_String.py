# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        start = list(start)
        end = list(end)
        i = 0
        j = 0
        while i < len(start):
            if start[i] == end[j]:
                i += 1
                j += 1
            else:
                pos = -1
                if end[j] == "R":
                    return False
                elif end[j] == "L":
                    for k in range(i, len(start)):
                        if start[k] == "R":
                            return False
                        if start[k] == "L":
                            pos = k
                            break
                else:
                    for k in range(i, len(start)):
                        if start[k] == "L":
                            return False
                        if start[k] == "X":
                            pos = k
                            break
                if pos == -1:
                    return False
                start[i], start[pos] = start[pos], start[i]
                i += 1
                j += 1
        return True



def main():
    s = Solution()
    print(s.canTransform("XXRXLXRXXX", "XXRLXXXXXR"))
    print(s.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
    print(s.canTransform("XRXL", "RLXX"))


if __name__ == "__main__":
    main()
