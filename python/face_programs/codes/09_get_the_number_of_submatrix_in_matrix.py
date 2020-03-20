# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from data_structure.stack import Stack


def get_the_number_of_submatrix_in_matrix(mat):
    max_area = 0
    length_of_column = len(mat[0])
    height = list(range(length_of_column))
    for i in range(length_of_column):
        height[i] = 0
    for row in mat:
        for index in range(length_of_column):
            height[index] = height[index] + 1 if row[index] == 1 else 0
        max_area = get_max_area(height, max_area)
    return max_area


def get_max_area(height, max_area):
    stack = Stack()
    lenght = len(height)
    j = 0
    for index, data in enumerate(height):

        while(not stack.is_empty()) and height[stack.peek()] >= data:
            j = stack.pop()
            k = -1 if stack.is_empty() else stack.peek()
            max_area = max((index-k-1)*height[j], max_area)
        stack.push(index)
    while not stack.is_empty():
        j = stack.pop()
        k = -1 if stack.is_empty() else stack.peek()
        max_area = max((lenght-k-1)*height[j], max_area)
    max_area = max(lenght*height[j], max_area)
    return max_area


def main():
    # max_area = 0
    # height = [3, 4, 5, 4, 3, 6]
    # max_area = get_max_area(height, max_area)
    # print(max_area)
    mat = [
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0]
    ]
    max_area = get_the_number_of_submatrix_in_matrix(mat)
    print(max_area)


if __name__ == "__main__":
    main()
