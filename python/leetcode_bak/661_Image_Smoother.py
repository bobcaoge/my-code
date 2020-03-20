# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        column = len(M[0])
        ret = [[0]*column for x in range(row)]
        for i in range(row):
            for j in range(column):
                ret[i][j] = self.get_num_of_num_filter(M, i, j, row, column)
        return ret

    def get_num_of_num_filter(self, image, x, y, row, column):
        """
        :type image:list[list[int]]
        :type x: int
        :type y: int
        :type row: int
        :type column: int
        :rtype : int
        """
        ret = 0
        ret_num = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0<= i < row and 0 <= j < column:
                    ret += 1
                    ret_num += image[i][j]
        return math.floor(ret_num*1.0/ret)

    def imageSmoother1(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        column = len(M[0])
        ret = [[0]*column for x in range(row)]
        for i in range(column):
            # 更新第一行
            ret[0][i] = self.get_num_of_num_filter(M, 0, i, row, column)
            # 更新最后行
            ret[row-1][i] = self.get_num_of_num_filter(M, row-1, i, row, column)

        for i in range(row):
            # 更新第一列
            ret[i][0] = self.get_num_of_num_filter(M, i, 0, row, column)
            # 更新最后一列
            ret[i][column-1] = self.get_num_of_num_filter(M, i, column-1, row, column)
        # print(row, column)
        for i in range(1, row-1):
            num_filter = sum(M[i-1][:3]) + sum(M[i][:3])+sum(M[i+1][:3])
            for j in range(1, column-1):
                ret[i][j] = math.floor(num_filter/9.0)
                # print(num_filter, i, j)
                try:
                    num_filter += M[i-1][j+2] + M[i][j+2] + M[i+1][j+2] - M[i-1][j-1] - M[i][j-1] - M[i+1][j-1]
                except:
                    # print("error")
                    pass
            # print("==========")

        return ret




def main():
    s = Solution()
    # print(s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
    # print(s.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
    print(s.imageSmoother([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))


if __name__ == "__main__":
    main()
