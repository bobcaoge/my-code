# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_length(self, head):
        ret = 0

        while head:
            ret += 1
            head = head.next
        return ret

    def reverse(self, head, length):
        front = None
        cur = head
        next = cur.next
        while length > 0:
            length -= 1
            cur.next = front
            front = cur
            cur = next
            next = cur.next

        # print(front, cur)
        return front, cur


    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = self.get_length(head)
        if length <= 1:
            return True
        half = int(length/2)
        # print(head.val)
        left, right = self.reverse(head, half)
        if length%2 == 1:
            right = right.next

        while left:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True



def main():
    s = Solution()
    head=ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    print(s.isPalindrome(head))

if __name__ == "__main__":
    main()
