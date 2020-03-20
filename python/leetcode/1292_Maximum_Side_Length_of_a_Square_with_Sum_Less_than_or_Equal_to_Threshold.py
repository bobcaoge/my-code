# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        row = len(mat)
        col = len(mat[0])
        ret = 0
        for i in range(1, row):
            mat[i][0] += mat[i-1][0]
        for j in range(1, col):
            mat[0][j] += mat[0][j-1]
        for i in range(1, row):
            for j in range(1, col):
                mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]

        for i in range(row):
            for j in range(col):
                k = ret

                while i+k < row and j+k < col:
                    s =mat[i+k][j+k] -(mat[i-1][j+k] if i-1 >= 0 else 0) - \
                       (mat[i+k][j-1] if j-1 >= 0 else 0) + \
                       (mat[i-1][j-1] if i-1 >= 0 and j-1>=0 else 0)
                    if s <= threshold:
                        ret = max(ret, k+1)
                    else:
                        break
                    k += 1
        return ret


def main():
    s = Solution()
    print(s.maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))
    print(s.maxSideLength(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1))
    print(s.maxSideLength(mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6))


if __name__ == "__main__":
    main()
