# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        stack = [root]
        while stack:
            if stack[-1].left:
                stack.append(stack[-1].left)
                stack[-2].left= None
            else:
                if stack[-1].right:
                    stack.append(stack[-1].right)
                    stack[-2].right = None
                else:
                    ret.append(stack.pop().val)
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
