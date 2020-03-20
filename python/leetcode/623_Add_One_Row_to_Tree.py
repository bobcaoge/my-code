# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        d -= 1
        def traverse(r, depth):
            if depth == d:
                left = r.left
                right = r.right
                r.left = TreeNode(v)
                r.left.left = left
                r.right = TreeNode(v)
                r.right.right = right
            else:
                traverse(r.left, depth+1)
                traverse(r.right, depth+1)
        if d == 0:
            ret = TreeNode(v)
            ret.left = root
            return ret
        traverse(root, 1)
        return root




def main():
    s = Solution()


if __name__ == "__main__":
    main()
