# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        m = {}
        index = 0
        while head:
            key = hash(head)
            if m.get(key, -1) != -1:
                return m[key]
            m[key] = index
            index += 1
            head = head.next
        return -1


def main():
    s = Solution()
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1
    print(s.detectCycle(head))


if __name__ == "__main__":
    main()
