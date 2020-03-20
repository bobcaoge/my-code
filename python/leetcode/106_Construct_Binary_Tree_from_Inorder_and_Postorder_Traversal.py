# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def traverse(self, inorder, postorder, start_of_inorder, end_of_inorder, start_of_postorder, end_of_postorder):
        if end_of_inorder == start_of_inorder:
            return TreeNode(postorder[end_of_postorder])

        elif end_of_inorder > start_of_inorder:
            root = TreeNode(postorder[end_of_postorder])
            length = inorder.index(postorder[end_of_postorder]) - start_of_inorder
            left = self.traverse(inorder, postorder, start_of_inorder, start_of_inorder+length-1, start_of_postorder, start_of_postorder+length-1)
            right = self.traverse(inorder, postorder, start_of_inorder+length+1, end_of_inorder, start_of_postorder+length, end_of_postorder-1)
            root.left = left
            root.right = right
            return root
        return None

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.traverse(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
