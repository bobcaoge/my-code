# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        dp = [[2000000]*(T+1) for _ in range(T+1)]
        for start, end in clips:
            end = min(end, T)
            for i in range(start, end+1):
                for j in range(i+1, end+1):
                    dp[i][j] = 1
        for i in range(T, -1, -1):
            for j in range(i, T+1):
                if dp[i][j] != 1:
                    dp[i][j] = min(dp[i][k]+dp[k][j] for k in range(i+1, j))
        return dp[0][T] if dp[0][T] != 2000000 else -1


def main():
    s = Solution()
    print(s.videoStitching(clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9))
    print(s.videoStitching([[0,4],[2,8]]
    ,5))


if __name__ == "__main__":
    main()
