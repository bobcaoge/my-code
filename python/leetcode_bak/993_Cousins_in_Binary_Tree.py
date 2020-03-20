# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_parent(self, root, target, depth=0):
        """
        :type root:TreeNode
        :type target:int
        :type depth:int
        :return: list[TreeNode, depth]
        """
        if root:
            if root.left and root.left.val == target:
                return [root, depth+1]
            if root.right and root.right.val == target:
                return [root, depth+1]
            left = self.get_parent(root.left, target, depth+1)
            right = self.get_parent(root.right, target, depth+1)
            return left or right

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if x == y or root.val == x or root.val == y:
            return False
        x_info = self.get_parent(root, x)

        y_info = self.get_parent(root, y)
        if x_info[1] == y_info[1] and x_info[0] != y_info[0]:
            return True
        return False


def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(s.isCousins(root, 3, 4))

if __name__ == "__main__":
    main()
