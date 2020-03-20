# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        cups = [[0 for j in range(i+1)] for i in range(100)]
        cups[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                cups[i+1][j] += max(cups[i][j]-1, 0)/2.0
                cups[i+1][j+1] += max(cups[i][j]-1, 0)/2.0
        return min(cups[query_row][query_glass], 1)


def main():
    s = Solution()
    print(s.champagneTower(1,1,1))


if __name__ == "__main__":
    main()
