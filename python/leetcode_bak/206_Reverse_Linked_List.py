# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        front = None
        cur = head
        tail = cur.next
        while tail:
            cur.next = front
            front = cur
            cur = tail
            tail = tail.next
        cur.next = front
        return cur



def main():
    s = Solution()


if __name__ == "__main__":
    main()
