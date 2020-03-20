# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        difficulties = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        difficulties.sort()
        ret = 0
        index_of_worker = 0
        index_of_diffculties = 0
        cur_profit = 0
        worker.sort()

        while index_of_worker < len(worker) and index_of_diffculties < len(difficulties):
            if worker[index_of_worker] >= difficulties[index_of_diffculties][0]:
                cur_profit = max(cur_profit, difficulties[index_of_diffculties][1])
                index_of_diffculties += 1
            else:
                # print(cur_profit)
                ret += cur_profit
                index_of_worker += 1

        return ret+(len(worker)-index_of_worker)*cur_profit


def main():
    s = Solution()
    print(s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))
    print(s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7,11]))


if __name__ == "__main__":
    main()
