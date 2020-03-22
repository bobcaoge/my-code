# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for row, col in reservedSeats:
            graph[row].add(col)
        ret = 0
        left = set()
        left.update([2,3,4,5])
        mid = set()
        mid.update([4,5,6,7])
        right = set()
        right.update([6,7,8,9])
        for i in graph:
            if i not in graph:
                ret += 2
            else:
                if not (graph[i] & left):
                    ret += 1
                    if not(graph[i] & right):
                        ret += 1
                elif not(graph[i] & mid):
                    ret += 1
                elif not(graph[i] & right):
                    ret += 1
        return ret + 2*(n-len(graph))


def main():
    s = Solution()
    print(s.maxNumberOfFamilies(3,[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))


if __name__ == "__main__":
    main()
