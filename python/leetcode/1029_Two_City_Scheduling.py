# /usr/bin/python2.7
# -*- coding:utf-8 -*-


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        def compare(a, b):
            c = abs(a[1]-a[0])-abs(b[1]-b[0])
            if c == 0:
                return 0
            if c>0:
                return 1
            return -1
        costs.sort(compare)
        even = len(costs)/2
        odd = even
        ret = 0
        for cost in costs[-1::-1]:
            if even == 0:
                odd -= 1
                ret += cost[0]
                continue
            if odd == 0:
                even -= 1
                ret += cost[1]
                continue

            if cost[0] < cost[1]:
                odd -= 1
                ret += cost[0]
            else:
                even -= 1
                ret += cost[1]

        return ret


def main():
    s = Solution()
    print(s.twoCitySchedCost([[10,20],[300,200],[400,50],[30,20]]))


if __name__ == "__main__":
    main()
