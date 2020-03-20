# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = collections.Counter(T)
        ret = ""
        for c in S:
            if m.get(c, 0) > 0:
                ret += c*m[c]
                m[c] = 0
        for c, count in m.items():
            if count != 0:
                ret += c*count
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
