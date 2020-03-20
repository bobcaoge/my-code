# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        parentheses = []
        for i, c in enumerate(s):
            if c in "()":
                parentheses.append((i, c))
        stack = []
        invalid = set()
        for i, c in parentheses:
            if c == "(":
                stack.append((i,c))
            else:
                if stack:
                    stack.pop()
                else:
                    invalid.add((i,c))
        invalid |= set(stack)
        return "".join([c for i, c in enumerate(s) if (i, c) not in invalid])


def main():
    s = Solution()
    print(s.minRemoveToMakeValid( "lee(t(c)o)de)"))


if __name__ == "__main__":
    main()
