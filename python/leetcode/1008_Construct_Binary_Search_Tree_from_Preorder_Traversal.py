# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def construct(start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(preorder[start])

            root = TreeNode(preorder[start])
            if preorder[start+1] > preorder[start]:
                root.right = construct(start+1, end)
                return root
            edge = end
            for i in range(start+1, end+1):
                if preorder[i] > preorder[start]:
                    edge = i-1
                    break
            root.left = construct(start+1, edge)
            root.right = construct(edge+1, end)
            return root
        return construct(0, len(preorder)-1)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
