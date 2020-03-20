# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        column = len(A[0])
        print(row, column)
        ret = [[0]*row for i in range(column)]
        print(ret)
        for i in range(row):
            for j in range(column):
                ret[j][i] = A[i][j]
        return ret


def main():
    s = Solution()
    print(s.transpose([[1,2,3],[4,5,6]]))


if __name__ == "__main__":
    main()
