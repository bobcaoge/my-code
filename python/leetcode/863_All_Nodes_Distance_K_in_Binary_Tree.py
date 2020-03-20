# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = {}
        def dfs(r):
            if r.left:
                graph[r] = graph.get(r, [])+[r.left]
                graph[r.left] = graph.get(r.left, [])+[r]
                dfs(r.left)
            if r.right:
                graph[r] = graph.get(r, [])+[r.right]
                graph[r.right] = graph.get(r.right, [])+[r]
                dfs(r.right)

        dfs(root)
        visited = set()
        visited.add(target)
        keep = [target]

        for i in range(K-1):
            buff = []
            for node in keep:
                for n in graph[node]:
                    if n not in visited:
                        buff.append(n)
                        visited.add(n)
            keep = buff
        return [node.val for node in keep]


def main():
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print(s.distanceK(root, root.left, 3))



if __name__ == "__main__":
    main()
