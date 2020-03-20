# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        intervals = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append((c, i))
            else:
                if stack:
                    while intervals and stack[-1][1] < intervals[-1][0]:
                        intervals.pop()
                    if intervals and intervals[-1][-1] + 1 == stack[-1][1]:
                        buff = intervals.pop()
                        intervals.append([buff[0], i])
                    else:
                        intervals.append([stack[-1][1], i])
                    stack.pop()
        return max([y - x for x, y in intervals])+1 if intervals else 0



def main():
    s = Solution()
    # print(s.longestValidParentheses("())(())"))
    print(s.longestValidParentheses(")(())(()()))("))
    print(s.longestValidParentheses("())()()"))


if __name__ == "__main__":
    main()
