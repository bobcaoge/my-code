# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0]*n
        cols = [0]*m
        ret = 0
        for row, col in indices:
            rows[row] += 1
            cols[col] += 1

        for i in range(n):
            for j in range(m):
                ret += 1 if (rows[i] + cols[j]) % 2 == 1 else 0
        return ret


def main():
    s = Solution()
    print(s.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))


if __name__ == "__main__":
    main()
