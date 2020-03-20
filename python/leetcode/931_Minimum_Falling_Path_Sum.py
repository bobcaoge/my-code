# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                temp = 2**31
                for gap in range(-1, 2):
                    if 0 <= j+gap < len(A[0]):
                        temp = min(temp, A[i-1][j+gap])
                A[i][j] = temp+A[i][j]
        return min(A[-1])

def main():
    s = Solution()
    print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.minFallingPathSum([[-80,-13,22],[83,94,-5],[73,-48,61]]))


if __name__ == "__main__":
    main()
