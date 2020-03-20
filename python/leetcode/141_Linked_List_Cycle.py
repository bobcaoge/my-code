# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        first = head.next
        second = head
        while first:
            if first == second:
                return True
            try:
                first = first.next.next
                second = second.next
            except:
                return False
        return False



def main():
    s = Solution()
    head = ListNode(3)
    cur = ListNode(2)
    head.next = cur
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    # head.next.next.next = cur
    print(s.hasCycle(head))


if __name__ == "__main__":
    main()
