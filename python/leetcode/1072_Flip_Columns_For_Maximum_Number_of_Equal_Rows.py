# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = {}
        for row in matrix:
            key = tuple(row)
            if m.get(key, 0) != 0:
                m[key] += 1
            else:
                key = tuple(1-x for x in row)
                if m.get(key, 0) != 0:
                    m[key] += 1
                else:
                    m[key] = 1
        return max(x for _, x in m.items())

    def maxEqualRowsAfterFlips1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        ret = 0
        for i in range(len(matrix)):
            buff = [""]*len(matrix[0])
            cnt = 0
            for j in range(len(matrix[0])):
                buff[j] = 1-matrix[i][j]
            for row in matrix:
                if row == buff or row == matrix[i]:
                    cnt += 1
            ret = max(ret, cnt)
        return ret



def main():
    s = Solution()
    print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))


if __name__ == "__main__":
    main()
