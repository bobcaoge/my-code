# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_height(self, root):
        if root:
            return max(self.get_height(root.left), self.get_height(root.right))+1
        return 0

    def printTree(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.get_height(root)
        ret = [["" for i in range(2**height-1)] for j in range(height)]

        def dfs(root, depth, pos):
            if root:
                ret[depth][((1<<(height-depth-1))-1)+(1<<(height-depth))*pos] = root.val
                dfs(root.left, depth+1, pos<<1)
                dfs(root.right, depth+1, (pos<<1)+1)
        dfs(root, 0, 0)
        return ret


def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(s.printTree(root))



if __name__ == "__main__":
    main()
