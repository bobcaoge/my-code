# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)+" "


class Solution(object):
    def reverse(self, head, length):
        before = head.next
        cur = before.next
        after = cur.next
        keep = before
        while length-2 > 0:
            cur.next = before
            before = cur
            cur = after
            after = after.next
        if head:
            keep.next = after
            head.next = cur
            return head
        else:
            keep.next = after
            return cur

    def reverseBetween1(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        front_head = None
        front_tail = None
        reversed_head = None
        reversed_tail = None
        back_head = None
        for i in range(1, n+1):
            node = head
            head = head.next
            node.next = None
            if i < m:
                if front_head is None:
                    front_head = node
                    front_tail = node
                else:
                    front_tail.next = node
                    front_tail = node
            elif i <= n:
                if reversed_head is None:
                    reversed_head = node
                    reversed_tail = node
                else:
                    node.next = reversed_head
                    reversed_head = node
                back_head = head
        if m == 1:
            reversed_tail.next = back_head
            return reversed_head
        else:
            front_tail.next = reversed_head
            reversed_tail.next = back_head
            return front_head

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n or not head:
            return head

        cur = head
        for i in range(2, m):
            cur = cur.next
        if m == 1:
            front = None
            cur = head
        else:
            front = cur
            cur = front.next
        # print(front)

        before = None
        after = cur.next
        for i in range(n-m):
            cur.next = before
            before = cur
            cur = after
            after = after.next

        # print(before, cur, after)
        cur.next = before
        # print(front, before, cur, after)

        if m == 1:
            head.next = after
            return cur
        else:
            front.next.next = after
            front.next = cur
            return head


def traverse(head):
    while head:
        print(head.val, end=" ")
        head = head.next


def main():
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    new_head = s.reverseBetween(head, 3, 4)
    traverse(new_head)



if __name__ == "__main__":
    main()
