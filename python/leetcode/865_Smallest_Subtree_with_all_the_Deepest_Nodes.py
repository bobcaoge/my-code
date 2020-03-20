# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        depth = self.get_depth(root)
        return self.dfs(root, 0, depth)

    def get_depth(self, root, depth=0):
        if root:
            left = self.get_depth(root.left, depth+1)
            right = self.get_depth(root.right, depth+1)
            return max(left, right, depth)
        return 0

    def dfs(self, root, depth, target_depth):
        if depth == target_depth:
            return root
        if root:
            left = self.dfs(root.left, depth+1, target_depth)
            right = self.dfs(root.right, depth+1, target_depth)
            if left and right:
                return root
            return left or right
        return None




def main():
    s = Solution()


if __name__ == "__main__":
    main()
