# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        stack = []
        num = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                    num += 1
        left = s.count('(')-num
        right = s.count(')')-num
        ret = set()
        dp = [[False, 0] for _ in range(len(s))]
        if s[-1] == '(':
            dp[-1] = [False, -1]
        elif s[-1] == ')':
            dp[-1] = [True, 1]
        else:
            dp[-1] = [True, 0]

        for i in range(len(s)-2, -1, -1):
            flag, num = dp[i+1]
            if flag:
                if s[i] == '(':
                    num += -1
                elif s[i] == ')':
                    num += 1
                if num < 0:
                    flag = False
                dp[i] = [flag, num]

        def dfs(exp, pos, L, R, num_of_left):
            if num_of_left < 0:
                return
            if pos >= len(s):
                if L == R == 0 and num_of_left == 0:
                    ret.add(exp)
                return
            if L == R == 0:
                flag, num_of_right = dp[pos]
                if flag and num_of_left == num_of_right:
                    ret.add(exp+s[pos:])
                return
            if s[pos] == '(':
                if left > 0:
                    dfs(exp, pos+1, L-1, R, num_of_left)
                dfs(exp+'(', pos+1, L, R, num_of_left +1)
            elif s[pos] == ')':
                if right > 0:
                    dfs(exp, pos+1, L, R-1, num_of_left)
                dfs(exp+')', pos+1, L, R, num_of_left-1)
            else:
                dfs(exp+s[pos], pos+1, L, R, num_of_left)
        dfs("", 0, left, right, 0)
        return list(ret)


def main():
    s = Solution()
    print(s.removeInvalidParentheses('p(r)'))
    print(s.removeInvalidParentheses('()())()'))
    print(s.removeInvalidParentheses(')('))
    print(s.removeInvalidParentheses("(a)())()"))
    print(s.removeInvalidParentheses("())v)(()(((((())"))
    print(s.removeInvalidParentheses(")()m)(((()((()(((("))


if __name__ == "__main__":
    main()
