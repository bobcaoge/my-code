# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from heapq import heappush, heappop


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        row = len(matrix)
        column = len(matrix[0])
        heappush(heap, [matrix[0][0], 0, 0])
        ret = 0
        for i in range(k):
            ret, r, c = heappop(heap)
            if c+1 < column:
                heappush(heap, [matrix[r][c+1], r, c+1])
            if c == 0 and r+1 < row:
                heappush(heap, [matrix[r+1][c], r+1, c])
        return ret


def main():
    s = Solution()
    print(s.kthSmallest(matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ],
        k = 8,))


if __name__ == "__main__":
    main()
