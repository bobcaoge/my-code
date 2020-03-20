# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def traverse(self, root, leaves):
        if root:
            self.traverse(root.left, leaves)
            if not root.left and not root.right:
                leaves.append(root.val)
                return leaves
            self.traverse(root.right, leaves)
            return leaves

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.traverse(root1, []) == self.traverse(root2, [])


def main():
    s = Solution()


if __name__ == "__main__":
    main()
