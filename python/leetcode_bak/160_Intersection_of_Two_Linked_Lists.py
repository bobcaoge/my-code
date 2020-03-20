# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length_a = 1
        length_b = 1
        if headA is None or headB is None:
            return
        curA = headA
        curB = headB
        while curA.next:
            curA = curA.next
            length_a += 1
        while curB.next:
            curB = curB.next
            length_b += 1
        print(length_a, length_b)
        if length_b > length_a:
            long_node_list = headB
            short_node_list = headA
            diff = length_b - length_a
            common = length_a
        else:
            long_node_list = headA
            short_node_list = headB
            diff = length_a - length_b
            common = length_b

        if curA == curB:
            for i in range(diff):
                long_node_list = long_node_list.next
            for i in range(common):
                if long_node_list == short_node_list:
                    return long_node_list
                else:
                    long_node_list = long_node_list.next
                    short_node_list = short_node_list.next






def main():
    s = Solution()


if __name__ == "__main__":
    main()
