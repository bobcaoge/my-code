# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def traverse(self, root):
        if root:
            if root.left and root.right:
                left_robbed, left_not_robbed = self.traverse(root.left)
                right_robbed, right_not_robbed = self.traverse(root.right)
                cur_robbed = left_not_robbed + right_not_robbed + root.val
                cur_not_robbed = max(left_not_robbed+right_not_robbed, left_not_robbed+right_robbed, left_robbed+right_not_robbed, left_robbed+right_robbed)
                return cur_robbed, cur_not_robbed
            elif root.left:
                left_robbed, left_not_robbed = self.traverse(root.left)
                cur_robbed = left_not_robbed + root.val
                cur_not_robbed = max(left_not_robbed, left_robbed)
                return cur_robbed, cur_not_robbed
            elif root.right:
                right_robbed, right_not_robbed = self.traverse(root.right)
                cur_robbed = right_not_robbed + root.val
                cur_not_robbed = max(right_not_robbed, right_robbed)
                return cur_robbed, cur_not_robbed
            else:
                return root.val, 0


    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.traverse(root))




def main():
    s = Solution()


if __name__ == "__main__":
    main()
