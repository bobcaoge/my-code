# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [TreeNode(0)]
        queue = [root]
        while queue:
            buff = []
            for node in queue:
                self.nodes.append(node)
                if node.left:
                    buff.append(node.left)
                if node.right:
                    buff.append(node.right)
            queue = buff



    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        self.nodes.append(TreeNode(v))
        i, mod = divmod(len(self.nodes)-1, 2)
        if mod == 0:
            self.nodes[i].left = self.nodes[-1]
        else:
            self.nodes[i].right = self.nodes[-1]
        return self.nodes[i].val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[1]




def main():

    s = CBTInserter(TreeNode(1))
    print([node.val for node in s.nodes[1:]])
    print(s.insert(2))
    print([node.val for node in s.nodes[1:]])
    print(s.get_root().val)
    print(s.get_root().left.val)


if __name__ == "__main__":
    main()
