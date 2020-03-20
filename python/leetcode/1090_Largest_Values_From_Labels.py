# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        items = sorted(zip(values, labels), reverse=True)
        m = collections.Counter()
        ret = 0
        for value, label in items:
            if num_wanted == 0:
                break
            if m[label] < use_limit:
                ret += value
                m[label] += 1
                num_wanted -= 1
        return ret


def main():
    s = Solution()
    print(s.largestValsFromLabels(values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1))
    print(s.largestValsFromLabels(values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2))
    print(s.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1))
    print(s.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2))



if __name__ == "__main__":
    main()
