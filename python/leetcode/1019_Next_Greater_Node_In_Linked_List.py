# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        length = self.get_length(head)
        values = [0]*length
        heap = []
        i = 0
        while head:

            while heap and heap[0][0] < head.val:
                values[heap[0][1]] = head.val
                heapq.heappop(heap)
            heapq.heappush(heap, [head.val, i])

            i += 1
            head = head.next
        return values





def main():
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(3)
    head.next.next = ListNode(6)
    print(s.nextLargerNodes(head))


if __name__ == "__main__":
    main()
