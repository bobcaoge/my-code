# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max([self.maxDepth(child) for child in root.children]+[0])+1


def main():
    s = Solution()


if __name__ == "__main__":
    main()
