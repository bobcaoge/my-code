# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        row = len(matrix)
        column = len(matrix[0])
        # down right
        ret = [[10000 for j in range(column)] for i in range(row)]
        def manager(first, second):
            for i in range(row):
                for j in range(column):
                    first[i][j] = min(first[i][j], second[i][j])

        record = [[10000 for j in range(column)] for i in range(row)]
        record[0][0] = 0 if matrix[0][0] == 0 else 10000
        for j in range(1, column):
            record[0][j] = 0 if matrix[0][j] == 0 else record[0][j-1]+1
        for i in range(1, row):
            record[i][0] = 0 if matrix[i][0] == 0 else record[i-1][0]+1
        for i in range(1, row):
            for j in range(1, column):
                record[i][j] = 0 if matrix[i][j] == 0 else  min(record[i-1][j], record[i][j-1])+1
        manager(ret, record)
        # print(record)

        record = [[10000 for j in range(column)] for i in range(row)]
        record[row-1][column-1] = 0 if matrix[row-1][column-1] == 0 else 10000
        for i in range(row-2, -1, -1):
            record[i][column-1] = 0 if matrix[i][column-1] == 0 else record[i+1][column-1]+1
        for j in range(column-2, -1, -1):
            record[row-1][j] = 0 if matrix[row-1][j] == 0 else record[row-1][j+1]+1
        for i in range(row-2, -1, -1):
            for j in range(column-2, -1, -1):
                record[i][j] = 0 if matrix[i][j] == 0 else min(record[i+1][j], record[i][j+1])+1
        manager(ret, record)
        # print(record)

        record = [[10000 for j in range(column)] for i in range(row)]
        record[0][column-1] = 0 if matrix[0][column-1] == 0 else 10000
        for i in range(1, row):
            record[i][column-1] = 0 if matrix[i][column-1] == 0 else record[i-1][column-1]+1
        for j in range(column-2, -1, -1):
            record[0][j] = 0 if matrix[0][j] == 0 else record[0][j+1]+1
        for i in range(1, row):
            for j in range(column-2, -1, -1):
                record[i][j] = 0 if matrix[i][j] == 0 else min(record[i-1][j], record[i][j+1])+1
        manager(ret, record)
        # print(record)

        record = [[10000 for j in range(column)] for i in range(row)]
        record[row-1][0] = 0 if matrix[row-1][0] == 0 else 10000
        for i in range(row-2, -1, -1):
            record[i][0] = 0 if matrix[i][0] == 0 else record[i+1][0]+1
        for j in range(1, column):
            record[row-1][j] = 0 if matrix[row-1][j] == 0 else record[row-1][j-1]+1
        for i in range(row-2, -1, -1):
            for j in range(1, column):
                record[i][j] = 0 if matrix[i][j] == 0 else min(record[i+1][j], record[i][j-1])+1
        manager(ret, record)
        # print(record)
        return ret


def main():
    s = Solution()
    print(s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
    print(s.updateMatrix([[1,1,1],[1,0,1],[1,1,1]]))



if __name__ == "__main__":
    main()
