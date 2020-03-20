# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    traverse_str = []

    def traverse(self, root):
        if root is None:
            self.traverse_str.append(" ")
            return
        self.traverse(root.left)
        self.traverse_str.append(root.val)
        self.traverse(root.right)

    def isSymmetric(self, root):
        if root and root.left and root.right:
            if root.left.val != root.right.val:
                return False
        self.traverse_str = []
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.traverse(root)
        print(self.traverse_str)
        # self.traverse_str = [-57,67,-97,4,-97,67,-57,]
        length = len(self.traverse_str)
        start = 0
        end = length-1
        while start < end:
            # print(start, end)
            if self.traverse_str[start] != self.traverse_str[end]:
                return False
            start += 1
            end -= 1

        return True



def main():
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(s.isSymmetric(root))
    #
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.right = TreeNode(3)
    # root.right.right = TreeNode(3)
    # print(s.isSymmetric(root))
    #
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(3)
    # # root.right.right = TreeNode(3)
    # root.right.left = TreeNode(2)
    # print(s.isSymmetric(root))

if __name__ == "__main__":
    main()
