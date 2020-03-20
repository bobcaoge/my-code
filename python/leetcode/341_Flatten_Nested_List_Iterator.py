# /usr/bin/python3.6
# -*- coding:utf-8 -*-


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested_list = nestedList
        self.ret = self.manage(nestedList)
        self.length = len(self.ret)
        self.cur_index = 0

    def manage(self, nested_list):
        ret = []
        for nested_integer in nested_list:
            if nested_integer.isInteger():
                ret.append(nested_integer.getInteger())
            else:
                ret.extend(self.manage(nested_integer.getList()))
        return ret

    def next(self):
        """
        :rtype: int
        """
        self.cur_index += 1
        return self.ret[self.cur_index-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_index < self.length


def main():
    pass


if __name__ == "__main__":
    main()
