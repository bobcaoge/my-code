# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        min_num = 2**32
        for i in range(m):
            for j in range(n):
                min_num = min(matrix[i][j], min_num)
        flag = min_num - 1
        # 将含有0的行都替换成 flag 但 保留零
        for i in range(m):
            if 0 in matrix[i]:
                for j in range(n):
                    if matrix[i][j] != 0:
                        matrix[i][j] = flag
        # print(matrix)
        # 将含有0的列都地换成flag 但保留0
        for j in range(n):
            contain_zero = False
            for i in range(m):
                if matrix[i][j] == 0:
                    contain_zero = True
                    break
            if contain_zero:
                for i in range(m):
                    matrix[i][j] = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == flag:
                    matrix[i][j] = 0
        print(matrix)


def main():
    s = Solution()
    s.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])
    s.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])
    s.setZeroes([[]])


if __name__ == "__main__":
    main()
