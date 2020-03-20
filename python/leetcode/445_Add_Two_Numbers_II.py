# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def get_length_of_linked_list(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def add(self, long, short):
        """
        :type long: ListNode
        :type short: ListNode
        :return:
        """
        if not long.next and not short.next:
            result = long.val + short.val
        else:
            result = long.val + short.val + self.add(long.next, short.next)

        long.val = result % 10
        return result / 10

    def add_2(self, head, carry, depth, cur):

        if cur != depth:
            result = head.val + carry
        else:
            result = head.val + self.add_2(head.next, carry, depth, cur+1)
        head.val = result % 10
        return result / 10

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        length_of_l1 = self.get_length_of_linked_list(l1)
        length_of_l2 = self.get_length_of_linked_list(l2)
        long = None
        short = None
        if length_of_l1 > length_of_l2:
            long = l1
            short = l2
        else:
            long = l2
            short = l1
        diff = abs(length_of_l2-length_of_l1)
        cursor_of_long = long
        while diff != 0:
            cursor_of_long = cursor_of_long.next
            diff -= 1
        diff = abs(length_of_l2-length_of_l1)
        carry = self.add(cursor_of_long, short)
        if diff != 0:
            carry = self.add_2(long, carry, abs(length_of_l2-length_of_l1), 1)
        if carry > 0:
            head = ListNode(carry)
            head.next = long
            return head
        return long

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 or l2

        stack1 = []
        while l1:
            stack1.append(l1)
            l1 = l1.next

        stack2 = []
        while l2:
            stack2.append(l2)
            l2 = l2.next
        carry = 0
        head = None
        while stack1 or stack2 or carry > 0:
            a = 0
            b = 0
            cur_node = None
            if stack1:
                cur_node = stack1.pop()
                a = cur_node.val

            if stack2:
                cur_node = stack2.pop()
                b = cur_node.val
            cur_value=(a+b+carry) % 10
            carry = (a+b+carry) / 10

            if not cur_node:
                cur_node = ListNode(cur_value)
            else:
                cur_node.val = cur_value
            cur_node.next = head
            head = cur_node
        return head





def main():
    s = Solution()


if __name__ == "__main__":
    main()
