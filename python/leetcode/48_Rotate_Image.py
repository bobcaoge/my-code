# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def rotate_point(self, matrix, x, y, x0, y0):

        if y <= y0:
            b = x0-x
            a = y0-y
            first_x = int(x0-a)
            first_y = int(y0+b)
            second_x = int(x0+b)
            second_y =int(y0+a)
            third_x = int(x0+a)
            third_y = int(y0-b)
            matrix[x][y], matrix[first_x][first_y], matrix[second_x][second_y], matrix[third_x][third_y] =\
                 matrix[third_x][third_y] , matrix[x][y], matrix[first_x][first_y], matrix[second_x][second_y]
        else:
            a = x0-x
            b = y-y0
            first_x = int(x0+b)
            first_y = int(y0+a)
            second_x =int(x0+a)
            second_y =int(y0-b)
            third_x = int(x0-b)
            third_y = int(y0-a)
            matrix[x][y], matrix[first_x][first_y], matrix[second_x][second_y], matrix[third_x][third_y] = \
                matrix[third_x][third_y] , matrix[x][y], matrix[first_x][first_y], matrix[second_x][second_y]

    def rotate_point1(self, matrix, x, y, x0, y0):

        if y <= y0:
            b = abs(x-x0)
            a = abs(y-y0)
            matrix[x][y], matrix[int(x0-a)][int(y0+b)], matrix[int(x0+b)][int(y0+a)], matrix[int(x0+a)][int(y0-b)] =\
                matrix[int(x0+a)][int(y0-b)], matrix[x][y], matrix[int(x0-a)][int(y0+b)], matrix[int(x0+b)][int(y0+a)]
            # print([x, y], [int(x0-a),int(y0+b)], [int(x0+b),int(y0+a)], [int(x0+a),int(y0-b)])
        else:
            a = abs(x-x0)
            b = abs(y-y0)
            matrix[x][y],  matrix[int(x0+b)][int(y0+a)], matrix[int(x0+a)][int(y0-b)], matrix[int(x0-b)][int(y0-a)] \
            = matrix[int(x0-b)][int(y0-a)], matrix[x][y],  matrix[int(x0+b)][int(y0+a)], matrix[int(x0+a)][int(y0-b)]
            # print([x,y],  [int(x0+b),int(y0+a)], [int(x0+a), int(y0-b)], [int(x0-a),int(y0-b)] )


    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)-1
        x0 = length / 2.0
        for i in range(length):
            for j in range(i, length-i):
                # print(i, j)
                self.rotate_point(matrix, i, j, x0, x0)





def main():
    s = Solution()
    matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(matrix)
    print(matrix)
    matrix =[
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    s.rotate(matrix)
    print(matrix)
    # s.rotate_point([], 0, 0, 1 , 1)
    # s.rotate_point([], 0, 1, 1 , 1)


if __name__ == "__main__":
    main()
