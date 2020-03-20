# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [[20000000]*4 for _ in range(366)]
        index = {day:i for i, day in enumerate(days)}
        for i in range(1, days[-1]+1):
            if i not in days:
                continue
            for j in range(max(1, i-6), i):
                dp[i][0] = min(dp[j][2], dp[i][0])
            for j in range(max(i-29, 1), i):
                dp[i][0] = min(dp[j][3], dp[i][0])
            last_day_travel = index.get(i, 0) - 1
            if last_day_travel < 0:
                dp[i][1] = costs[0]
                dp[i][2] = costs[1]
                dp[i][3] = costs[2]
            else:
                dp[i][1] = min(dp[days[last_day_travel]][k] for k in range(4))+costs[0]
                dp[i][2] = min(dp[days[last_day_travel]][k] for k in range(4))+costs[1]
                dp[i][3] = min(dp[days[last_day_travel]][k] for k in range(4))+costs[2]

        return min(dp[days[-1]][i] for i in range(4))


def main():
    s = Solution()
    print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
    print(s.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
    print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [7,2,15]))


if __name__ == "__main__":
    main()
