#! /usr/bin/python3.6
# -*- coding:utf-8 -*-


def get_height_of_tree(root):
    if not root:
        return 0
    return max(get_height_of_tree(root.left), get_height_of_tree(root.right))+1


def main():
    pass


if __name__ == "__main__":
    main()