# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def get_height(root):
            if not root:
                return 0
            return max(get_height(root.left), get_height(root.right))+1

        self.height = get_height(root)

        def dfs(root, height):
            if not root:
                return None
            if height == self.height:
                return root
            left, right = dfs(root.left, height+1), dfs(root.right, height+1)
            return root if left and right else left or right

        return dfs(root, 1)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
