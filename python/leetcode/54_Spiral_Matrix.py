# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = []

    def get_one_circle(self, matrix, x, y, width, height):
        self.ret += matrix[x][y:y+width]
        for i in range(x+1, x+height-1):
            self.ret.append(matrix[i][y+width-1])
        if height > 1:
            self.ret += matrix[x+height-1][y:y+width][-1::-1]
        if width > 1:
            for i in range(x+height-2, x, -1):
                # print(self.ret)
                # print(i, y)
                self.ret.append(matrix[i][y])

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        self.ret = []
        row = len(matrix)
        column = len(matrix[0])
        lower = row if row < column else column
        length = int(lower / 2) if lower % 2 == 0 else int(lower/2+1)
        for i in range(length):
            self.get_one_circle(matrix, i, i, column-2*i, row-2*i)
            # break
        # print(self.ret)
        return self.ret


def main():
    s = Solution()
    print(s.spiralOrder([
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]))
    print(s.spiralOrder([
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]))
    print(s.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
    print(s.spiralOrder([[1,2,3,4,5,6,7]]))



if __name__ == "__main__":
    main()
