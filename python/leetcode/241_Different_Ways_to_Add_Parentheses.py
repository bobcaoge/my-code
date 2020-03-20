# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re

class Solution(object):


    def diffWaysToCompute(self, s):
        """
        :type s:str
        :rtype: List[int]
        """
        ret = []
        for i, c in enumerate(s):
            if c in {"+", "-", "*"}:
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i+1:])
                for n1 in left:
                    for n2 in right:
                        if c == "+":
                            ret.append(n1+n2)
                        elif c == "-":
                            ret.append(n1-n2)
                        else:
                            ret.append(n1*n2)
        if not ret:
            ret.append(int(s))
        return ret





def main():
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))
    print(s.diffWaysToCompute("2*3-4*5"))


if __name__ == "__main__":
    main()
