# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node:
    def __init__(self, val=0, s=0, letter=''):
        self.val = val
        self.sum = s
        self.letter = letter
        self.next = []

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
    def dfs(self, root, key, val, depth):
        """
        :type root:Node
        :type key: str
        :type val: int
        :type depth: int
        :return:
        """
        if depth == len(key):
            ret = val - root.val
            root.val = val
            return ret
        for node in root.next:
            if node.letter == key[depth]:
                cur = node
                add = self.dfs(node, key, val, depth+1)
                break
        else:
            cur = Node(0, 0, key[depth])
            root.next.append(cur)
            add = self.dfs(cur, key, val, depth+1)
        cur.sum += add
        return add


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.dfs(self.root, key, val, 0)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        def s(root, pre, depth):
            """
            :type root: Node
            :type pre: str
            :type depth: int
            :return:
            """
            if depth == len(pre):
                return root.sum
            for node in root.next:
                if node.letter == pre[depth]:
                    return s(node, pre, depth+1)
            return 0
        return s(self.root, prefix, 0)


def main():
    m = MapSum()
    m.insert("he", 10)
    m.insert("h", 10)
    print(m.sum("h"))
    m.insert("h", 100)
    print(m.sum("h"))
    print()


if __name__ == "__main__":
    main()
