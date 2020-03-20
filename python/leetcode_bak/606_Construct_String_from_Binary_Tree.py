# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        if root:
            left = self.tree2str(root.left)
            right = self.tree2str(root.right)
            if left and right:
                return str(root.val)+"("+left+")"+"("+right+")"
            elif left and not right:
                return str(root.val)+"("+left+")"
            elif not left and right:
                return str(root.val)+"()"+"("+right+")"
            else:
                return str(root.val)




def main():
    s = Solution()


if __name__ == "__main__":
    main()
