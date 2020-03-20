#! /usr/bin/python3.6
#-*- coding:utf-8 -*-

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Utils(object):
    def preorder_traverse(self, root):
        """
        :param root:
        :return:
        """
        def dfs(r):
            if r:
                dfs(r.left)
                print(r.val, end=' ')
                dfs(r.right)
        dfs(root)
        print()

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return

        def dfs(root):
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return
                dfs(root.left)
            elif root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return
                dfs(root.right)
        dfs(self.root)

    def get_max_val_node_of_bst(self, root, parent):
        if root:
            if root.right:
                return self.get_max_val_node_of_bst(root.right, root)
            return root, parent
        return None, parent

    def get_node_and_its_parent(self, val, root, parent):
        if root:
            if root.val == val:
                return [root, parent]
            if root.val > val:
                return self.get_node_and_its_parent(val, root.left, root)
            return self.get_node_and_its_parent(val, root.right, root)
        return None, None



    def remove(self, val, root):
        if not root:
            return None
        if root.val > val:
            root.left = self.remove(val, root.left)
        elif root.val < val:
            root.right = self.remove(val, root.right)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            left = root.left
            while left.right:
                left = left.right
            root.val = left
            root.left = self.remove(root.val, root.left)
        return root






def main():
    tree = BinarySearchTree()
    for num in [7,4,9,2,6,8,10,1,3,5]:
        tree.insert(num)
    util = Utils()
    util.preorder_traverse(tree.root)
    # tree.remove(4)
    # tree.remove(7)
    # tree.remove(3)
    tree.remove(1, tree.root)
    util.preorder_traverse(tree.root)


if __name__ == "__main__":
    main()