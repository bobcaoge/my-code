# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.manage()

    def manage(self):
        if not self.matrix:
            return
        row = len(self.matrix)
        column = len(self.matrix[0])
        for i in range(1, row):
            self.matrix[i][0] += self.matrix[i-1][0]
        for j in range(1, column):
            self.matrix[0][j] += self.matrix[0][j-1]
        for i in range(1, row):
            for j in range(1, column):
                self.matrix[i][j] += self.matrix[i-1][j] + self.matrix[i][j-1]- self.matrix[i-1][j-1]
        print(self.matrix)


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = self.matrix[row2][col2]
        if col1 > 0:
            ret -= self.matrix[row2][col1-1]
        if row1 > 0:
            ret -= self.matrix[row1-1][col2]
        if row1 > 0 and col1 > 0:
            ret += self.matrix[row1-1][col1-1]
        return ret


def main():
    pass


if __name__ == "__main__":
    main()
