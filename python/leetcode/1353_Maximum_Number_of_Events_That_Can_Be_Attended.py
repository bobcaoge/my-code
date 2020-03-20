# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        cur_day = 0
        ret = 0
        while events:
            start_day, end_day = events.pop(0)
            if start_day <= cur_day < end_day:
                to_insert = [cur_day+1, end_day]
                events.insert(bisect.bisect(events, to_insert), to_insert)
            elif start_day > cur_day:
                ret += 1
                cur_day = start_day

        return ret


def main():
    s = Solution()
    print(s.maxEvents([[1,2],[2,3],[3,4]]))
    print(s.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))
    print(s.maxEvents([[1,4],[1,1], [2,2],[3,3]]))


if __name__ == "__main__":
    main()
