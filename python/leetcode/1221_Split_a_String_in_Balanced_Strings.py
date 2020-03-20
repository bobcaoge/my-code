# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] == c:
                    stack.append(c)
                else:
                    stack.pop()
                    if not stack:
                        ret += 1
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
