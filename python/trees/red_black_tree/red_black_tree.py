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
    def adjust(self, cur):
        """
        :type cur:RBNode
        :return:
        """
        ret = cur
        if cur.is_black:
            # print(cur.val)
            if cur.left and cur.left.is_black is False:
                if cur.left.left and cur.left.left.is_black is False:
                    if cur.right is None or cur.right.is_black:
                        ret = self.single_left_rotation(cur)
                    else:
                        ret = self.recolor(cur)
                elif cur.left.right and cur.left.right.is_black is False:
                    if cur.right is None or cur.right.is_black:
                        ret = self.left_right_rotation(cur)
                    else:
                        ret = self.recolor(cur)
            if cur.right and cur.right.is_black is False:
                if cur.right.right and cur.right.right.is_black is False:
                    if cur.left is None or cur.left.is_black:
                        ret = self.single_right_rotation(cur)
                    else:
                        ret = self.recolor(cur)
                elif cur.right.left and cur.right.left.is_black is False:
                    if cur.left is None or cur.left.is_black:
                        ret = self.right_left_rotation(cur)
                    else:
                        ret = self.recolor(cur)
        return ret
    def insert(self, value):
        def insert_manager(r, val):
            """
            :type r:RBNode
            :param val:
            :return:
            """
            if r is None:
                return RBNode(val)
            elif r.val > val:
                r.left = insert_manager(r.left, val)
            elif r.val < val:
                r.right = insert_manager(r.right, val)
            return self.adjust(r)
        self.root = insert_manager(self.root, value)
        self.root.is_black = True

    def remove(self, value):
        def remove_manager(r, val):
            if r is None:
                return r
            elif r.val > val:
                r.left = remove_manager(r.left, val)
            elif r.val < val:
                r.right = remove_manager(r.right, val)
            else:
                if r.left is None:
                    return r.right
                if r.right is None:
                    return r.left
                left_max = r.left
                while left_max.right:
                    left_max = left_max.right
                r.val = left_max.val
                r.left = remove_manager(r.left, r.val)
            return r
        self.root = remove_manager(self.root, value)


def preorder_traverse_RBTree(root):
    """
    :type root:RBNode
    :param root:
    :return:
    """
    if not root:
        return [None]
    ret = [(root.val, root.is_black)]
    ret.extend(preorder_traverse_RBTree(root.left))
    ret.extend(preorder_traverse_RBTree(root.right))
    return ret


def main():
    rbt = RBTree()
    for i in range(9):
        rbt.insert(i)
    print(preorder_traverse_RBTree(rbt.root))
    rbt.remove(7)
    print(preorder_traverse_RBTree(rbt.root))



if __name__ == "__main__":
    main()

















