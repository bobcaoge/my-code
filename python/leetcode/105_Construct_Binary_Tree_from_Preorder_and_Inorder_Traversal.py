# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def traverse(self, preorder, inorder, start_of_preorder, end_of_preorder, start_of_inorder, end_of_inorder):
        if end_of_preorder == start_of_preorder:
            return TreeNode(preorder[start_of_preorder])

        elif end_of_preorder > start_of_preorder:
            root = TreeNode(preorder[start_of_preorder])
            length = inorder.index(preorder[start_of_preorder]) - start_of_inorder
            left = self.traverse(preorder, inorder, start_of_preorder+1, start_of_preorder+length, start_of_inorder, start_of_inorder+length-1)
            right = self.traverse(preorder, inorder, start_of_preorder+length+1, end_of_preorder, start_of_inorder+length+1, end_of_inorder)
            root.left = left
            root.right = right
            return root
        return None

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.traverse(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
    def buildTree1(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            root = TreeNode(preorder[0])
            index_of_root_in_inorder = inorder.index(preorder[0])
            left = self.buildTree(preorder[1:index_of_root_in_inorder+1], inorder[:index_of_root_in_inorder])
            right = self.buildTree(preorder[index_of_root_in_inorder+1:], inorder[index_of_root_in_inorder+1:])
            root.left = left
            root.right = right
            return root
        return None


def main():
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    head = s.buildTree(preorder, inorder)
    print(head)

if __name__ == "__main__":
    main()
