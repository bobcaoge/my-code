# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        column = len(matrix[0])
        start = 0
        end = column * len(matrix) - 1
        mid = int((start + end) / 2)
        while start <= end:
            cur = matrix[int(mid / column)][int(mid % column)]
            if cur == target:
                return True
            if cur > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = int((start + end) / 2)
        return False


def main():
    s = Solution()
    print(s.searchMatrix([[1,1]], 2))
    print(s.searchMatrix([[1],[3],[5]], 2))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],31))
    # m = 4
    # i = 0
    # while i <= 15:
    #     print(int(i/m), int(i%m))
    #     i+=1



if __name__ == "__main__":
    main()
