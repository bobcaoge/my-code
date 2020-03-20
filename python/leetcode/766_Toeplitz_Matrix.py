# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if 0<= i-1< row and 0<= j-1 < column:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True


def main():
    s = Solution()


if __name__ == "__main__":
    main()
