# /usr/bin/python3.6
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.x = 0
        self.d = 0
        self.ret = root.val
        def traverse(root, x_pos, depth):
            if root:
                if depth > self.d or depth == self.d and self.x > x_pos:
                    self.x = x_pos
                    self.d = depth
                    self.ret = root.val
                traverse(root.left, x_pos-1, depth+1)
                traverse(root.right, x_pos+1, depth+1)
        traverse(root, 0, 0)
        return self.ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
