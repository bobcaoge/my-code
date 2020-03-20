# /usr/bin/python2.7
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def get_length_of_linklist(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        middle = get_length_of_linklist(head) / 2
        for i in range(middle):
            head = head.next
        return head


def main():
    s = Solution()


if __name__ == "__main__":
    main()
