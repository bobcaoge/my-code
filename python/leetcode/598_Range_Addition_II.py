# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m*n
        min_row = ops[0][0]
        min_column = ops[0][1]
        for row, column in ops[1:]:
            min_row = min(min_row, row)
            min_column = min(min_column, column)
        if min_row > m:
            min_row = m
        if min_column > n:
            min_column = n
        return min_row*min_column



def main():
    s = Solution()


if __name__ == "__main__":
    main()
