# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        ret = []
        row = len(matrix)
        column = len(matrix[0])
        flag = True
        for i in range(row):
            x = i
            y = 0
            cur = []
            while 0 <= x < row and 0 <= y < column:
                cur.append(matrix[x][y])
                x -= 1
                y += 1
            ret.extend(cur if flag else cur[::-1])
            flag = not flag

        for j in range(1, column):
            x = row-1
            y = j
            cur = []
            while 0 <= x < row and 0 <= y < column:
                cur.append(matrix[x][y])
                x -= 1
                y += 1
            ret.extend(cur if flag else cur[::-1])
            flag = not flag
        return ret


def main():
    s = Solution()
    print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.findDiagonalOrder([[1,2,3],[4,5,6]]))
    print(s.findDiagonalOrder([[1,2],[3,4],[5,6]]))


if __name__ == "__main__":
    main()
