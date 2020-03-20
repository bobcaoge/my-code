# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import copy

class Solution(object):
    def manager(self, s):
        back = []
        for i, c in enumerate(s):
            if c == ")":
                back.append(i)
        ret = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                    temp = s[:i] + "(" + s[i:j]+")"+s[j:]
                    ret.add(temp)
        return ret



    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        ret = ["()"]
        ret = set(ret)
        for i in range(n-1):
            buff = set()
            while ret:
                buff |= self.manager(ret.pop())
            ret = buff
        return list(ret)






def main():
    s = Solution()
    print(s.generateParenthesis(4))
    # print(s.manager("(())"))
if __name__ == "__main__":
    main()
