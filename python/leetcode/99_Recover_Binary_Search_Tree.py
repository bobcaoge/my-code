# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        swapped = []
        self.last_node = TreeNode(-1<<31)
        def inorder_traverse(r):
            if r:
                inorder_traverse(r.left)
                if self.last_node.val > r.val:
                    swapped.append(self.last_node)
                    swapped.append(r)
                self.last_node = r
                inorder_traverse(r.right)
        inorder_traverse(root)
        swapped[0].val, swapped[-1].val = swapped[-1].val, swapped[0].val

def inorder_traverse(r):
    if r:
        inorder_traverse(r.left)
        print(r.val, end=" ")
        inorder_traverse(r.right)


def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    s.recoverTree(root)
    inorder_traverse(root)



if __name__ == "__main__":
    main()
