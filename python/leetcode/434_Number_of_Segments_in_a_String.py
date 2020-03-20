# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        last = False
        for c in s:
            if c != " " and not last:
                ret += 1
                last = True
            if c == " ":
                last = False
        return ret


def main():
    s = Solution()
    print(s.countSegments("   hello, my name is john"))
    print(s.countSegments("   hello "))
    print(s.countSegments(""))


if __name__ == "__main__":
    main()
