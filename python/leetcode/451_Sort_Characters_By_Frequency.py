# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        m = {}
        for c in s:
            count = m.get(c, 0)
            m[c] = count+1
        ret = ""
        for count, c in sorted([[count, c] for c, count in m.items()])[-1::-1]:
            ret += c*count
        return ret


def main():
    s = Solution()
    print(s.frequencySort("tree"))


if __name__ == "__main__":
    main()
