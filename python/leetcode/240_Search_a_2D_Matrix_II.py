# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        mid = (start+end)/2
        while start <= end:
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
            mid = (start+end)/2
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        for nums in matrix:
            flag = self.search(nums, target)
            if flag:
                return True
        return False


def main():
    s = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], s.searchMatrix(matrix, matrix[i][j]))
    print(s.searchMatrix([[-5]], -5))



if __name__ == "__main__":
    main()
