# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "n"
        ret = str(root.val)
        ret += ","+self.serialize(root.left)
        ret += ","+self.serialize(root.right)
        return ret


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == "n":
            return None
        node_values = data.split(',')
        root = TreeNode(int(node_values[0]))
        stack = [root]
        for value in node_values[1:]:
            if stack[-1] != "n":
                if value != "n":
                    stack[-1].left = TreeNode(value)
                    stack.append(stack[-1].left)
                else:
                    stack.append('n')
            else:
                if value == "n":
                    while stack[-1] == "n":
                        stack.pop()
                        stack.pop()
                    stack.append("n")
                else:
                    stack[-2].right = TreeNode(value)
                    stack.append(stack[-2].right)
        return root


def main():
    pass


if __name__ == "__main__":
    main()
