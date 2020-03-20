#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
def preorder_traverse(root):
    if not root:
        return [None]
    ret = [root.val]
    ret.extend(preorder_traverse(root.left))
    ret.extend(preorder_traverse(root.right))
    return ret


class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 0


class BalancedSearchTree(object):
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return -1 if node is None else node.height

    def single_left_rotation(self, A):
        """
        left left rotation
        :type A: TreeNode
        :rtype : TreeNode
        """
        B = A.left
        A.left = B.right
        B.right = A
        A.height = max(self.get_height(A.left), self.get_height(A.right))+1
        B.height = max(self.get_height(B.left), self.get_height(B.right))+1
        return B

    def single_right_rotation(self, root):
        """
        right right rotation
        :type root: TreeNode
        :rtype : TreeNode
        """
        right = root.right
        root.right = right.left
        right.left = root
        root.height = max(self.get_height(root.left), self.get_height(root.right))+1
        right.height = max(self.get_height(right.left), self.get_height(right.right))+1
        return right

    def left_right_rotation(self, root):
        root.left = self.single_right_rotation(root.left)
        return self.single_left_rotation(root)

    def right_left_rotation(self, root):
        root.right = self.single_left_rotation(root.right)
        return self.single_right_rotation(root)

    def insert(self, value):
        def insert_manager(r, val):
            ret = r
            if not r:
                return TreeNode(val)
            elif val > r.val:
                r.right = insert_manager(r.right, val)
                if abs(self.get_height(r.left) - self.get_height(r.right)) > 1:
                    if val > r.right.val:
                        ret = self.single_right_rotation(r)
                    else:
                        ret = self.right_left_rotation(r)
            elif val < r.val:
                r.left = insert_manager(r.left, val)
                if abs(self.get_height(r.left) - self.get_height(r.right)) > 1:
                    if val < r.left.val:
                        ret = self.single_left_rotation(r)
                    else:
                        ret = self.left_right_rotation(r)
            ret.height = max(self.get_height(ret.left), self.get_height(ret.right))+1
            return ret
        self.root = insert_manager(self.root, value)

    def adjust(self, root):
        if not root:
            return root
        h_of_left = self.get_height(root.left)
        h_of_right = self.get_height(root.right)
        # print('-----------before----------')
        # print(preorder_traverse(root))
        # print(root.val)
        if h_of_left - h_of_right > 1:
            if root.left.left.height > root.left.right.height:
                root = self.single_left_rotation(root)
            else:
                root = self.left_right_rotation(root)
        elif h_of_right - h_of_left > 1:
            if root.right.right.height > root.right.left.height:
                root = self.single_right_rotation(root)
            else:
                root = self.right_left_rotation(root)
        root.height = max(self.get_height(root.left), self.get_height(root.right))+1
        # print(preorder_traverse(ret))
        # print('---------after---------')
        return root

    def remove(self, value):
        def remove_value(root, val):
            if not root:
                return root
            ret = root
            if root.val < val:
                root.right = remove_value(root.right, val)
            elif root.val > val:
                root.left = remove_value(root.left, val)
            else:
                if root.left is None:
                    ret = root.right
                elif root.right is None:
                    ret = root.left
                else:
                    left_max = root.left
                    while left_max.right:
                        left_max = left_max.right
                    root.val = left_max.val
                    root.left = remove_value(root.left, root.val)
            ret = self.adjust(ret)
            return ret
        self.root = remove_value(self.root, value)
