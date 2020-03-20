# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_listNode(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        cur = None
        while l1 and l2:
            # print("====")
            # print_listNode(head)
            if l1.val < l2.val:
                if head is None:
                    head = l1
                    cur = head
                else:
                    cur.next = l1
                    cur = cur.next
                l1 = l1.next
            else:
                if head is None:
                    head = l2
                    cur = head
                else:
                    cur.next = l2
                    cur = cur.next
                l2 = l2.next
        if l1:
            if cur:
                cur.next = l1
            else:
                head = l1
        if l2:
            if cur:
                cur.next = l2
            else:
                head = l2
        return head




def main():
    s= Solution()
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    print_listNode(head1)
    print_listNode(head2)

    ret = s.mergeTwoLists(head1, head2)
    print_listNode(ret)


if __name__ == "__main__":
    main()
