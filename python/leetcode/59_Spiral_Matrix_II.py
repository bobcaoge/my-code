# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    start = 1
    def get_one_circle(self, matrix, x, width):
        matrix[x][x:x + width] = [a for a in range(self.start, self.start+width)]
        self.start += width
        for i in range(x + 1, x + width - 1):
            matrix[i][x + width - 1] = self.start
            self.start += 1
        if width > 1:
            matrix[x + width - 1][x:x + width] = [a for a in range(self.start+width-1, self.start-1, -1)]
            self.start += width
        if width > 1:
            for i in range(x + width - 2, x, -1):
                matrix[i][x] = self.start
                self.start += 1

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.start = 1
        if n % 2 == 0:
            row = n / 2
        else:
            row = (n-1)/2+1
        row = int(row)
        matrix = [[0]*n for i in range(n)]
        for i in range(row):
            self.get_one_circle(matrix,i,n-2*i)
        return matrix




def main():
    s = Solution()
    # print(s.generateMatrix(0))
    # print(s.generateMatrix(1))
    print(s.generateMatrix(3))
    # print(s.generateMatrix(4))


if __name__ == "__main__":
    main()
