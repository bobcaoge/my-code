# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 and root2:
            kids_of_root1 = [(root1.left.val if root1.left else -1), (root1.right.val if root1.right else -1)]
            kids_of_root2 = [(root2.left.val if root2.left else -1), (root2.right.val if root2.right else -1)]
            if kids_of_root1 == kids_of_root2:
                return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            elif kids_of_root1[::-1] == kids_of_root2:
                return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
            return False
        return root1 == root2




def main():
    s = Solution()


if __name__ == "__main__":
    main()
