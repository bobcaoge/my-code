# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        ret = 0
        for c in S:
            if c == "(":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    ret += 1
        return ret + len(stack)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
