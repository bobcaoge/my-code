# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        temp = []
        for child in root.children:
            temp.extend(self.postorder(child))
        return temp+[root.val]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
