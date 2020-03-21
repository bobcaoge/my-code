#! /usr/bin/python3.6
# -*- coding:utf-8 -*-
from red_black_tree.red_black_tree import RBNode

def preorder_traverse_RBTree(root):
    """
    :type root:RBNode
    :param root:
    :return:
    """
    if not root:
        return [None]
    ret = [root.val, root.is_black]
    ret.extend(preorder_traverse_RBTree(root.left))
    ret.extend(preorder_traverse_RBTree(root.right))
    return ret


