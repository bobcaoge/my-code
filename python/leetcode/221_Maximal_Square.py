# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def get_max_square(self, nums):
        stack = []
        square = 0
        for i, num in enumerate(nums):
            num = nums[i]
            while stack and nums[stack[-1]] >= num:
                j = stack.pop()
                height = nums[j]
                k = stack[-1] if stack else -1
                square = max(square, min(i-k-1, height)**2)
            stack.append(i)
        # print(stack)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            height = nums[j]
            square = max(square, min(len(nums)-k-1, height)**2)
        return square

    def maximalSquare1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if i == 0:
                    matrix[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] != "0":
                        matrix[i][j] = int(matrix[i][j]) + matrix[i-1][j]
                    else:
                        matrix[i][j] = 0
        ret = 0
        for nums in matrix:
            ret = max(ret, self.get_max_square(nums))
        return ret

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        column = len(matrix[0])
        dp = [[0]*column for _ in range(row)]
        ret = 0
        for i in range(row):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            if dp[i][0] == 1:
                ret = 1
        for j in range(column):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            if dp[0][j] == 1:
                ret = 1

        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                    ret = max(dp[i][j], ret)
        # print(dp)
        return ret*ret



def main():
    s = Solution()
    # print(s.get_max_square([3,1,3,2,2]))
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))


if __name__ == "__main__":
    main()
