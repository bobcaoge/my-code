class Solution:
    def calc(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        buff = [[0]*column for _ in range(row)]
        for j in range(column):
            if matrix[0][j] != 0:
                buff[0][j] = [matrix[0][j], -2**32]
            else:
                buff[0][j] = [-2**32, 0]
        for i in range(1, row):
            for j in range(column):
                buff[i][j] = [-2**32, -2**32]
                for x, y in {(i-1, j), (i-1, j-1), (i-1, j+1)}:
                    if 0<=y<column:
                        if matrix[i][j] != 0:
                            buff[i][j][0] = max(buff[i][j][0], buff[x][y][0])
                            buff[i][j][1] = max(buff[i][j][1], buff[x][y][1])
                        else:
                            buff[i][j][0] = max(buff[i][j][0], buff[x][y][1])
                            buff[i][j][1] = max(buff[i][j][1], buff[x][y][0])
                if matrix[i][j] != 0:
                    buff[i][j][0]+= matrix[i][j]
                    buff[i][j][1] += -matrix[i][j]
        return max([max(x) for x in buff[-1]])

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[8,9,10],[5,0,5],[-9,-8,-10],[0,1,2],[5,4,6]]
    print(s.calc(matrix))


