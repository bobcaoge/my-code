# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        index = 0
        m = {}
        cur = head
        copy_nodes = []
        while cur:
            m[hash(cur)] = index
            node = Node(cur.val, None, None)
            if copy_nodes:
                copy_nodes[-1].next = node
            copy_nodes.append(node)
            index += 1
            cur = cur.next
        cur = head
        copy_node = copy_nodes[0]
        while cur:
            if cur.random:
                copy_node.random = copy_nodes[m[hash(cur.random)]]
            cur = cur.next
            copy_node = copy_node.next
        return copy_nodes[0]

    def copyRandomList1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        values = []
        copy_nodes = []
        cur = head
        index = 0
        while cur:
            values.append(cur.val)
            node = Node(cur.val, None, None)
            if copy_nodes:
                copy_nodes[-1].next = node
            copy_nodes.append(node)
            cur.val = index
            cur = cur.next
            index += 1

        index = 0
        cur = head
        while cur:
            # print(cur.val)
            if cur.random is not None:
                copy_nodes[cur.val].random = copy_nodes[cur.random.val]
            # cur.val = values[index]
            cur = cur.next
            index += 1

        index = 0
        cur = head
        while cur:
            cur.val = values[index]
            cur = cur.next
            index += 1

        return copy_nodes[0]

def main():
    s = Solution()
    print(hash(Node(3, None, None)))

if __name__ == "__main__":
    main()
