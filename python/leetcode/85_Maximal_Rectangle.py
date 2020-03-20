# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
            """
            :type heights: List[int]
            :rtype: int
            """
            heights.append(0)
            stack = []
            ret = 0
            for i, height in enumerate(heights):
                pos = i
                while stack and stack[-1][0] > height:
                    ret = max(ret, stack[-1][0]*(i-stack[-1][-1]))
                    pos = stack.pop()[1]
                stack.append([height, pos])
            return ret
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        heights = [[0 for _ in range(col)] for __ in range(row)]
        for j in range(col):
            if matrix[0][j] == '1':
                heights[0][j] = 1

        for i in range(1, row):
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[i][j] = heights[i-1][j]+1
        ret = 0
        for line in heights:
            ret = max(ret, largestRectangleArea(line))
        return ret





def main():
    s = Solution()
    print(s.maximalRectangle([["1","0"],["1","0"]]))
    print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))


if __name__ == "__main__":
    main()
