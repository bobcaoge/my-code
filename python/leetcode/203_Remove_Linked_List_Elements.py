# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        if not head:
            return head
        front = None
        cur = head
        ret = head
        while cur:
            if cur.val == val:
                if front is None:
                    ret = ret.next
                else:
                    front.next = cur.next
                    # front = front.next?
            else:
                if front is None:
                    front = cur
                else:
                    front = front.next
            cur = cur.next

        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
