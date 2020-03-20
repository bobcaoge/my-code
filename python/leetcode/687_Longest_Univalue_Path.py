# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    length = 0

    def traverse(self, root):
        if not root:
            return 0
        ret = 1
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        left_flag = False
        right_flag = False
        if root.left and root.val == root.left.val:
            ret += left
            left_flag = True
        if root.right and root.val == root.right.val:
            ret += right
            right_flag = True
        self.length = max(ret, self.length)
        if left_flag and right_flag:
            return max(left, right)+1
        elif left_flag:
            return left+1
        elif right_flag:
            return right+1
        else:
            return 1

    def longestUnivaluePath(self, root: 'TreeNode') -> 'int':
        self.length = 0
        self.traverse(root)
        return self.length-1 if self.length != 0 else 0




def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(s.longestUnivaluePath(root))


if __name__ == "__main__":
    main()
