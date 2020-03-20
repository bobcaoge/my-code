# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def scoreOfParentheses1(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S == "":
            return 0
        if S == "()":
            return 1
        count = 0
        for index, c in enumerate(S):
            if c == "(":
                count += 1
            else:
                count -= 1
                if count == 0:
                    internal = self.scoreOfParentheses(S[1:index])
                    right = self.scoreOfParentheses(S[index+1:])
                    return (internal*2 if internal != 0 else 1) + right

    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        ret = 0
        count = 0
        move = True
        for c in S:
            if c == "(":
                count += 1
                move = True
            else:
                if move:
                    ret += 2**(count-1)
                count -= 1
                move = False
        return ret


def main():
    s = Solution()
    print(s.scoreOfParentheses("()"))
    print(s.scoreOfParentheses("(())"))
    print(s.scoreOfParentheses("(()(()))"))


if __name__ == "__main__":
    main()
