# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = head
        second = first.next
        third = second.next

        second.next = first
        first.next = third
        head = second

        before = first

        while before.next:
            # print_linklist(head)
            if before.next is None or before.next.next is None:
                break
            first = before.next
            second = first.next
            third = second.next

            second.next = first
            first.next = third
            before.next = second
            before = first


        return head
def print_linklist(head):
    """
    :type head: ListNode
    """
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


def main():
    s = Solution()


if __name__ == "__main__":
    main()
