# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def process(s, p, si, pi):
            if pi == len(p):
                return len(s) == si

            if pi+1 == len(p) or p[pi+1] != "*":
                return si != len(s) and (s[si] == p[pi] or p[pi] == '.') and process(s, p, si+1, pi+1)

            while si != len(s) and (s[si] == p[pi] or p[pi] == '.'):
                if process(s, p, si, pi+2):
                    return True
                si += 1
            return process(s, p, si, pi+2)

        if s is None or p is None:
            return False
        return process(s, p, 0, 0)


def main():
    s = Solution()
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("aa", "a"))


if __name__ == "__main__":
    main()
