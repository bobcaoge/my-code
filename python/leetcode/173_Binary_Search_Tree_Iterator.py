# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.g = self.inorder(root)
        self.length = 1 if root else 0

    def inorder(self, root):
        stack = []
        if root is None:
            yield None
        else:
            stack.append(root)
        self.length = 1
        while stack:
            if stack and stack[-1].left:
                stack.append(stack[-1].left)
                self.length += 1
                continue
            else:
                out = stack.pop()
                self.length -= 1
                if stack and out is stack[-1].left:
                    stack[-1].left = None
                if out.right:
                    stack.append(out.right)
                    self.length += 1
                yield out.val
        self.length = 0

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return next(self.g)


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.length > 0


def main():
    root = TreeNode(2)
    # root.left = TreeNode(1)
    # root.right = TreeNode(3)
    s = BSTIterator(root)
    print(s.hasNext())
    print(s.next())
    print(s.hasNext())
    # print(s.next())
    # print(s.hasNext())
    # print(s.next())
    # print(s.hasNext())
    # s.inorder()


if __name__ == "__main__":
    main()
