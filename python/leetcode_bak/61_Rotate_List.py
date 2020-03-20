# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def get_length(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        length = 0
        father = None
        cur = head
        while cur:
            length += 1
            father = cur
            cur = cur.next
        return length, father

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length, tail = self.get_length(head)
        if length == 0 or length == 1 or k == 0:
            return head
        num = length - k % length
        # print(num)
        if num == length:
            return head
        num -= 1
        if num == 0:
            first = head.next
            head.next = None
            tail.next = head
            return first

        cur = head
        while num != 0:
            cur = cur.next
            num -= 1
        first = cur.next
        cur.next = None
        tail.next = head
        return first



def main():
    s = Solution()


if __name__ == "__main__":
    main()
