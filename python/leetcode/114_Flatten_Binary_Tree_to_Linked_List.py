# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    nodes = []

    def get_nodes(self, root):
        if root:
            self.nodes.append(root)
            self.get_nodes(root.left)
            self.get_nodes(root.right)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.nodes = []
        self.get_nodes(root)
        for i in range(len(self.nodes)-1):
            self.nodes[i].left = None
            self.nodes[i].right = self.nodes[i+1]





def main():
    s = Solution()


if __name__ == "__main__":
    main()
