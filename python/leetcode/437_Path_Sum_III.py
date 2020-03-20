# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ret = 0

    def get(self, root, last, target):
        if root:
            if last + root.val == target:
                self.ret += 1
                return
            self.get(root.left, last+root.val, target)
            self.get(root.right, last+root.val, target)

    def traverse(self, root, target):
        if root:
            self.get(root, 0, target)
            self.traverse(root.left, target)
            self.traverse(root.right, target)

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.ret = 0
        self.traverse(root, target)
        return self.ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
