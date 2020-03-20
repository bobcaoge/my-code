# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):

    def buff(self, s):
        """
        # using DFS
        # find all single integers
        # as for the list in it , call self to manage
        :type s: str
        :rtype: NestedInteger
        """
        i = 0
        digits = ""
        ret = NestedInteger()
        while i < len(s):
            if "0" <= s[i] <= "9" or s[i] == "-":
                digits += s[i]
            else:
                if  digits:
                    num = int(digits)
                    buf = NestedInteger(num)
                    ret.add(buf)
                if s[i] == "[":
                    start = i
                    left = 1
                    i += 1
                    while i < len(s) and left > 0:
                        if s[i] == "[":
                            left += 1
                        elif s[i] == "]":
                            left -= 1
                        i += 1
                    i -= 1
                    ret.add(self.buff(s[start+1:i]))
                digits = ""
            i += 1
        if digits:
            ret.add(NestedInteger(int(digits)))
        return ret

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        if not s:
            return NestedInteger()
        if s[0] != "[":
            return NestedInteger(int(s))
        return self.buff(s[1:-1])


def main():
    s = Solution()
    a = s.deserialize("[1,2,3,4]")
    print(a)
    # print(s.manage([a]))


if __name__ == "__main__":
    main()
