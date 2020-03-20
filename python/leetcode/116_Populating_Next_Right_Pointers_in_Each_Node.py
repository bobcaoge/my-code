# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    nodes_of_every_level = []

    def traverse(self, root, depth):
        if root:
            if depth < len(self.nodes_of_every_level):
                self.nodes_of_every_level[depth].next = root
                self.nodes_of_every_level[depth] = root
            else:
                self.nodes_of_every_level.append(root)
            self.traverse(root.left, depth+1)
            self.traverse(root.right, depth+1)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.nodes_of_every_level = []
        self.traverse(root, 0)
        return root

    def traverse1(self, root, depth):
        if root:
            if depth < len(self.nodes_of_every_level):
                self.nodes_of_every_level[depth].append(root)
            else:
                self.nodes_of_every_level.append([root])
            self.traverse1(root.left, depth+1)
            self.traverse1(root.right , depth+1)

    def connect1(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.nodes_of_every_level = []
        self.traverse(root, 0)
        for nodes in self.nodes_of_every_level:
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
        return root


def main():
    s = Solution()


if __name__ == "__main__":
    main()
