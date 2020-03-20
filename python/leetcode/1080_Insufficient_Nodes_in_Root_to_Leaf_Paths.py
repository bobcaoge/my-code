# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def dfs(root, val):
            if not root:
                return True
            remove_left = dfs(root.left, root.val+val)
            remove_right = dfs(root.right, root.val+val)
            is_leaf = not root.left and not root.right
            if remove_left:
                root.left = None
            if remove_right:
                root.right = None
            if is_leaf:
                return val + root.val < limit
            return remove_right and remove_left

        return root if dfs(root, 0) else None









def main():
    s = Solution()


if __name__ == "__main__":
    main()
