# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def valid_column_max(x, y):
            for i in range(len(matrix)):
                if matrix[i][y] < matrix[x][y]:
                    return False
            return True

        ret = []
        for i in range(len(matrix)):
            cur_col = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] < matrix[i][cur_col]:
                    cur_col = j
            if valid_column_max(i, cur_col):
                ret.append(matrix[i][cur_col])
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
