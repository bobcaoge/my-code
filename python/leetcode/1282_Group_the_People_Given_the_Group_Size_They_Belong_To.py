# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        m = collections.defaultdict(list)
        for i, group in enumerate(groupSizes):
            if not m[group]:
                m[group].append([i])
            else:
                if len(m[group][-1]) < group:
                    m[group][-1].append(i)
                else:
                    m[group].append([i])
        ret = []
        for _, x in m.items():
            ret.extend(x)
        return ret


def main():
    s = Solution()
    print(s.groupThePeople([3,3,3,3,3,1,3]))


if __name__ == "__main__":
    main()
