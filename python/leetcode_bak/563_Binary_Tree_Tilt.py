# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def traverse(self,root):
        """
        :type root:TreeNode
        :param root:
        :return:
        """
        if not root.left and not root.right:
            return [root.val, 0]
        elif not root.left and root.right:
            right = self.traverse(root.right)
            right[1] += abs(right[0])
            right[0] += root.val
            return right
        elif not root.right and root.left:
            left = self.traverse(root.left)
            left[1] += abs(left[0])
            left[0] += root.val
            return left
        else:
            left = self.traverse(root.left)
            right = self.traverse(root.right)
            return [left[0]+right[0]+root.val, abs(left[0]-right[0])+left[1]+right[1]]
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root)[1] if root else 0


def main():
    s = Solution()


if __name__ == "__main__":
    main()
