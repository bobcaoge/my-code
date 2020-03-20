# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ret = 0

    def traverse(self, root, sum_of_before_str):
        if root:
            sum_of_before_str += str(root.val)
            if not root.left and not root.right:
                self.ret += int(sum_of_before_str)
            else:
                if root.left:
                    self.traverse(root.left, sum_of_before_str)
                if root.right:
                    self.traverse(root.right, sum_of_before_str)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.traverse(root, "")
        return self.ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
