# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def is_a_triangle(self, x, y, z):
        return x+y > z and x+z > y and y+z > x

    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        A.sort()
        for i in range(length-2):
            x = A[length-i-1]
            y = A[length-i-2]
            z = A[length-i-3]
            if self.is_a_triangle(x,y,z):
                return x + y + z
        return 0
    def largestPerimeter1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        max_perimeter = 0
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if self.is_a_triangle(A[i], A[j], A[k]):
                        max_perimeter = max(max_perimeter, A[i]+A[j]+A[k])
        return max_perimeter


def main():
    s = Solution()


if __name__ == "__main__":
    main()
