# /usr/bin/python3.6
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        length_left = self.maxDepth(root.left)
        length_right = self.maxDepth(root.right)
        return max(length_left, length_right) + 1



def main():
    s = Solution()
    root = TreeNode(3)
    root.right = TreeNode(20)
    root.left = TreeNode(9)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    print(s.maxDepth(root))


if __name__ == "__main__":
    main()
