# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.nodes = []
        def dfs(root):
            if root:
                dfs(root.left)
                self.nodes.append(root)
                dfs(root.right)

        def generate_balanced_tree(start, end):
            if start > end:
                return None
            mid = (start+end)//2
            self.nodes[mid].left = generate_balanced_tree(start, mid-1)
            self.nodes[mid].right = generate_balanced_tree(mid+1, end)
            return self.nodes[mid]
        dfs(root)
        return generate_balanced_tree(0, len(self.nodes)-1)



def main():
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(s.balanceBST(root))


if __name__ == "__main__":
    main()
