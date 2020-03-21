#! /usr/bin/python3.6
# -*- coding:utf-8 -*-
from .red_black_tree import RBTree
from utils.utils_of_red_black_tree import preorder_traverse_RBTree


def main():
    rbt = RBTree()
    for i in range(10):
        rbt.insert(i)
    preorder_traverse_RBTree(rbt.root)



if __name__ == "__main__":
    main()