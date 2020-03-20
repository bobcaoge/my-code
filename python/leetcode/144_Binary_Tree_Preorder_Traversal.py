# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        stack = [root]
        ret.append(root.val)
        while stack:
            left = stack[-1].left
            if left:
                ret.append(left.val)
                stack.append(left)
                continue
            right = stack[-1].right
            if right:
                ret.append(right.val)
                stack.append(right)
                continue
            if len(stack) == 1:
                break
            if stack[-1] == stack[-2].left:
                stack[-2].left = None
            else:
                stack[-2].right = None
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
