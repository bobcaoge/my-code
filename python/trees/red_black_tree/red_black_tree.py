#! /usr/bin/python3.6
# -*- coding:utf-8 -*-


class RBNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.is_black = False


class RBTree(object):
    def __init__(self):
        self.root = None

    def single_left_rotation(self, cur):
        """
        :type cur: RBNode
        :return:
        """
        left = cur.left
        cur.left = left.right
        left.right = cur
        cur.is_black = False
        left.is_black = True
        return left

    def single_right_rotation(self, cur):
        """
        :type cur: RBNode
        :return:
        """
        right = cur.right
        cur.right = right.left
        right.left = cur
        cur.is_black = False
        right.is_black = True
        return right


    def left_right_rotation(self, cur):
        """
        :type cur:RBNode
        :return:
        """
        cur.left = self.single_left_rotation(cur.left)
        return self.single_right_rotation(cur)

    def right_left_rotation(self, cur):
        """
        :type cur:RBNode
        :return:
        """
        cur.right = self.single_right_rotation(cur.right)
        return self.single_left_rotation(cur)

    def recolor(self, cur):
        """
        :type cur:RBNode
        :return:
        """
        cur.is_black = False
        cur.left.is_black = True
        cur.right.is_black = True
        return cur

    def insert(self, value):
        def insert_manager(r, val):
            """
            :type r:RBNode
            :param val:
            :return:
            """
            ret = r
            if r is None:
                return RBNode(val)
            elif r.val > val:
                r.left = insert_manager(r.left, val)
            elif r.val < val:
                r.right = insert_manager(r.right, val)
            if r.is_black:
                if r.left and r.left.is_black is False:
                    if r.left.left and r.left.left.is_black is False:
                        if r.right is None or r.right.is_black:
                            ret = self.single_left_rotation(r)
                        else:
                            ret = self.recolor(r)
                    elif r.left.right and r.left.right.is_black is False:
                        if r.right is None or r.right.is_black:
                            ret = self.left_right_rotation(r)
                        else:
                            ret = self.recolor(r)
                elif r.right and r.right.is_black is False:
                    if r.right.right and r.right.right.is_black is False:
                        if r.left is None or r.left.is_black:
                            ret = self.single_right_rotation(r)
                        else:
                            ret = self.recolor(r)
                    elif r.right.left and r.right.left.is_black is False:
                        if r.left is None or r.left.is_black:
                            ret = self.right_left_rotation(r)
                        else:
                            ret = self.recolor(r)
            return ret
        self.root = insert_manager(self.root, value)



import utils.utils_of_red_black_tree as urb


def main():
    rbt = RBTree()
    for i in range(10):
        rbt.insert(i)
    urb.preorder_traverse_RBTree(rbt.root)



if __name__ == "__main__":
    main()

















