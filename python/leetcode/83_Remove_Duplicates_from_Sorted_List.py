# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def print_listNode(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


def generate_node_list(node_values):
    # node_values = []
    head = None
    cur = head
    for value in node_values:
        if head is None:
            head = ListNode(value)
            cur = head
        else:
            cur.next = ListNode(value)
            cur = cur.next
    print_listNode(head)
    return head


def main():
    s = Solution()
    print_listNode(s.deleteDuplicates(generate_node_list([1,1,2])))
    print_listNode(s.deleteDuplicates(generate_node_list([1,1,2,3,3])))



if __name__ == "__main__":
    main()
