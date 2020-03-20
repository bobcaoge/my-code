# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def generate_reflection(self, row, col):
        ret = []
        flag = True
        for i in range(row):
            start = i*col+1
            cur = [x for x in range(start, start+col)]
            ret.insert(0, cur if flag else cur[::-1])
            flag = not flag
        return {ret[i][j]: (i, j) for i in range(row) for j in range(col)}

    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        m = self.generate_reflection(row, col)
        heap = [[0, 1]]
        target = row*col
        visited =[True]*(target+1)
        while heap:
            step, num= heapq.heappop(heap)
            if num == target:
                return step
            for i in range(1, 7):
                if num + i <= target:
                    x, y = m[num+i]
                    j = num + i if board[x][y] == -1 else board[x][y]
                    if visited[j]:
                        visited[j] = False
                        heapq.heappush(heap, [step+1, j])





def main():
    s = Solution()
    print(s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))


if __name__ == "__main__":
    main()
