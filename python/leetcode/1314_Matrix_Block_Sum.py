# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        ret = []
        for i in range(row):
            cur = []
            cur_sum = 0
            for x in range(i-K, i+K+1):
                for y in range(0, K):
                    if row> x >= 0 and 0<= y < col:
                        cur_sum += mat[x][y]
            for j in range(K, col+K):
                for x in range(i-K, i+K+1):
                    cur_sum += mat[x][j] if row> x >= 0 and col> j>=0 else 0
                    cur_sum -= mat[x][j-2*K-1] if row> x >= 0 and col> j-2*K-1 >=0 else 0
                cur.append(cur_sum)
            ret.append(cur)
        return ret


def main():
    s = Solution()
    print(s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],2))


if __name__ == "__main__":
    main()
