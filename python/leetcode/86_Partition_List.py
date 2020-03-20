# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = None
        bigger_head = None
        less_tail = None
        bigger_tail = None
        while head:

            node = head
            head = head.next
            node.next = None

            if node.val < x:
                if less_head is None:
                    less_head = node
                    less_tail = node
                else:
                    less_tail.next = node
                    less_tail = node
            else:
                if bigger_head is None:
                    bigger_head = node
                    bigger_tail = node
                else:
                    bigger_tail.next = node
                    bigger_tail = node

        if less_head:
            less_tail.next = bigger_head
            return less_head
        return bigger_head


def main():
    s = Solution()


if __name__ == "__main__":
    main()
