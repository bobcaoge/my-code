# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        height = len(A)
        for i, row in enumerate(A):
            if row[0] == 0:
                self.toggle_row(A, i)
        for j in range(len(A[0])):
            if self.count_one_of_col(A, j)*2 < height:
                self.toggle_col(A, j)

        ret = 0
        for row in A:
            ret += self.binary2oct(row)
        return ret

    def binary2oct(self, arr):
        ret = 0
        for num in arr:
            ret = (ret << 1) + num
        return ret
    def count_one_of_col(self, matrix, j):
        ret = 0
        for i in range(len(matrix)):
            if matrix[i][j] == 1:
                ret += 1
        return ret

    def toggle_col(self, matrix, j):
        for i in range(len(matrix)):
            matrix[i][j] = 1-matrix[i][j]

    def toggle_row(self, matrix, i):
        for j in range(len(matrix[0])):
            matrix[i][j] = 1- matrix[i][j]


def main():
    s = Solution()
    print(s.matrixScore([[0,1],[0,1],[0,1],[0,0]]))



if __name__ == "__main__":
    main()
