# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if n == length:
            return head.next

        n = length - n
        cur = head
        while n != 1:
            cur = cur.next
            n -= 1
        cur.next = cur.next.next
        return head


def main():
    s = Solution()


if __name__ == "__main__":
    main()
