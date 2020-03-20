# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        sub_tree = {} # serialization:treeNode
        ret = set()

        def dfs(r):
            if not r:
                return "n "
            right = dfs(r.right)
            left = dfs(r.left)
            key = str(r.val)+" "+left+right
            if sub_tree.get(key, None):
                ret.add(key)
            else:
                sub_tree[key] = r
            return key
        dfs(root)
        return [sub_tree[x] for x in ret]




def main():
    s = Solution()


if __name__ == "__main__":
    main()
