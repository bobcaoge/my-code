# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = set()
        q = [node]
        m = {}
        while q:
            cur_node = q.pop()
            if cur_node not in visited:
                m[cur_node] = Node(cur_node.val, [])
                visited.add(cur_node)
            if cur_node.neighbors:
                for neighbor in cur_node.neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
        for cur_node in visited:
            for neighbor in cur_node.neighbors:
                m[cur_node].neighbors.append(m[neighbor])
                q.append(neighbor)
        return m[node]






def main():
    s = Solution()


if __name__ == "__main__":
    main()
