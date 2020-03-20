# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    ret = []
    def traverse(self, root, layer):
        if root:
            if layer < len(self.ret):
                self.ret[layer].append(root.val)
            else:
                self.ret.append([root.val])
            for child in root.children:
                self.traverse(child, layer+1)

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        self.ret = []
        self.traverse(root, 0)
        return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
