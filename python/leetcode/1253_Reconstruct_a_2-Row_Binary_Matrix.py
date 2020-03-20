# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        ret = [[0 for j in range(len(colsum))] for i in range(2)]

        for col, val in enumerate(colsum):
            if val == 2:
                ret[0][col] = 1
                ret[1][col] = 1
                upper -= 1
                lower -= 1
            if upper < 0 or lower < 0:
                return []

        for col, val in enumerate(colsum):
            if val == 1:
                if upper > 0:
                    upper -= 1
                    ret[0][col] = 1
                elif lower > 0:
                    lower -= 1
                    ret[1][col] = 1
                else:
                    return []
        return ret if upper == 0 and lower == 0 else []



def main():
    s = Solution()
    print(s.reconstructMatrix(4,
    7,
    [2,1,2,2,1,1,1]))


if __name__ == "__main__":
    main()
