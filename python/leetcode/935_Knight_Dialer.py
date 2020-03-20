# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [[1]*3 for _ in range(4)]
        dp[3][0] = dp[3][2] = 0
        for i in range(N-1):
            dp = self.move(dp)

        return sum([sum(x) for x in dp]) % (10**9+7)

    def move(self, grid):
        """
        :type grid:list[list[int]]
        :return:
        """
        row = len(grid)
        col = len(grid[0])
        num = 1000000007
        buff_grid = [[0]*col for _ in range(row)]
        buff_grid[0][0] = (grid[1][2] + grid[2][1]) % num
        buff_grid[0][1] = (grid[2][0] + grid[2][2]) % num
        buff_grid[0][2] = (grid[1][0] + grid[2][1]) % num
        buff_grid[1][0] = (grid[0][2] + grid[2][2] + grid[3][1]) % num
        buff_grid[1][1] = 0
        buff_grid[1][2] = (grid[0][0] + grid[2][0] + grid[3][1]) % num
        buff_grid[2][0] = (grid[0][1] + grid[1][2]) % num
        buff_grid[2][1] = (grid[0][0] + grid[0][2]) % num
        buff_grid[2][2] = (grid[0][1] + grid[1][0]) % num
        buff_grid[3][1] = (grid[1][0] + grid[1][2]) % num

        return buff_grid




def main():
    s = Solution()
    print(s.knightDialer(1))
    print(s.knightDialer(2))
    print(s.knightDialer(3))
    print(s.knightDialer(5000))


if __name__ == "__main__":
    main()
