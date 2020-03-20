# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        def get(i, j):
            buff = []
            di = 0
            while i+di < len(mat) and j+di < len(mat[0]):
                buff.append(mat[i+di][j+di])
                di += 1
            buff.sort(reverse=True)
            di = 0
            while i+di < len(mat) and j+di < len(mat[0]):
                mat[i+di][j+di] = buff.pop()
                di += 1
        for i in range(len(mat)):
            get(i, 0)
        for j in range(1, len(mat[0])):
            get(0, j)
        return mat


def main():
    s = Solution()
    print(s.diagonalSort([[9,8,7],[6,5,4],[3,2,1]]))


if __name__ == "__main__":
    main()
