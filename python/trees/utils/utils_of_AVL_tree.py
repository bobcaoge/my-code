#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
from balanced_search_tree.AVLTree import TreeNode


def valid_AVLTree(root):
    def valid(r):
        if r is None:
            return 0, True
        height_of_left, flag_of_left = valid(r.left)
        height_of_right, flag_of_right = valid(r.right)
        if abs(height_of_left-height_of_right) > 1 or (not flag_of_left) or (not flag_of_right):
            return 0, False
        return max(height_of_right, height_of_left)+1, True
    return valid(root)[1]


def preorder_traverse(root):
    if not root:
        return [None]
    ret = [root.val]
    ret.extend(preorder_traverse(root.left))
    ret.extend(preorder_traverse(root.right))
    return ret

def main():
    pass


if __name__ == "__main__":
    main()