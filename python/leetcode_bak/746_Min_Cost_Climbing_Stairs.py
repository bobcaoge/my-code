# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def calc_cost(self, cost):
        step = cost[0]
        not_step = 0
        for i in range(1, len(cost)):
            cur_step = min(not_step+cost[i], step+cost[i])
            cur_not_step = min(step, not_step+cost[i-1])
            step, not_step = cur_step, cur_not_step
        return min(step, not_step)

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        return self.calc_cost(cost)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
