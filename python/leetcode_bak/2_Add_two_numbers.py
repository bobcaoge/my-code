# /usr/bin/python3.6
# -*- coding:utf-8 -*-
# Definition for singly-linked list.


class ListNode(object):

     def __init__(self, x):
         self.val = x
         self.next = None


def reverse(head):
    """
    :type head: ListNode
    :param head:
    :return:
    """
    if head is None:
        return head
    if head.next is None:
        return head
    if head.next.next is None:
        buffer = head.next
        buffer.next = head
        head.next = None
        return buffer
    front = head
    cur = head.next
    tail = cur.next
    front.next = None
    while tail is not None:
        cur.next = front
        front = cur
        cur = tail
        tail = tail.next
    cur.next = front
    return cur

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ordered_l1 = l1
        ordered_l2 = l2

        add_next = 0
        ret = ListNode(0)
        cur = ret
        while ordered_l1 is not None or ordered_l2 is not None:
            # print(ordered_l1.val, ordered_l2.val)
            add1 = 0
            add2 = 0
            if ordered_l1 is not None:
                add1 = ordered_l1.val
                ordered_l1 = ordered_l1.next
            if ordered_l2 is not None:
                add2 = ordered_l2.val
                ordered_l2 = ordered_l2.next

            add = add1 + add2 + add_next
            # print(add)
            num = add % 10
            add_next = int(add/10)
            cur.next = ListNode(num)
            # print(num, add_next)
            cur = cur.next
        if add_next != 0:
            cur.next = ListNode(add_next)


        return ret.next








def print_listNode(head):
    """
    :type head: ListNode
    :param head:
    :return:
    """
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

def main():
    # head = ListNode(2)
    # head.next = ListNode(4)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(5)
    # head.next.next.next.next = ListNode(6)
    # print_listNode(head)
    # buffer = reverse(head)
    # print_listNode(buffer)

    s = Solution()
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(3)

    root = ListNode(5)
    root.next = ListNode(6)
    root.next.next = ListNode(4)

    ret = s.addTwoNumbers(head, root)
    print_listNode(ret)

    head = ListNode(1)
    head.next = ListNode(8)
    # print_listNode(reverse(head))
    root = ListNode(0)

    ret = s.addTwoNumbers(head, root)
    print_listNode(ret)

if __name__ == "__main__":
    main()
