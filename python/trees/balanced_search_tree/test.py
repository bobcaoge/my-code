#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
from balanced_search_tree.AVLTree import BalancedSearchTree
import utils.utils_of_AVL_tree as ua


def main():
    avl = BalancedSearchTree()
    for i in range(10):
        avl.insert(i)
    print(ua.valid_AVLTree(avl.root))
    print(ua.preorder_traverse(avl.root))
    avl.remove(0)
    print(ua.valid_AVLTree(avl.root))
    print(ua.preorder_traverse(avl.root))
    avl.remove(2)
    print(ua.valid_AVLTree(avl.root))
    print(ua.preorder_traverse(avl.root))



if __name__ == "__main__":
    main()