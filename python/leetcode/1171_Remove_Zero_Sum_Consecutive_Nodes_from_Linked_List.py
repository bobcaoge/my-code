# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        record = {} # sum : cur_node
        m = {} # cur_node: sum
        pre_head = ListNode(-1)
        pre_head.next = head
        cursor = pre_head
        s = 0
        while cursor.next:
            # print(cursor.val, "=====", s)
            # traverse(pre_head.next)
            record[s] = cursor
            m[cursor] = s
            s += cursor.next.val
            if record.get(s, -1) != -1:
                # print(cursor.next.val, s)
                start = record[s].next
                while start != cursor.next:
                    del record[m[start]]
                    start = start.next
                record[s].next = cursor.next.next
                cursor = record[s]
            else:
                cursor = cursor.next
        return pre_head.next


def traverse(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

def main():
    s = Solution()
    head = ListNode(0)
    head.next = ListNode(0)

    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(-3)
    # head.next.next.next.next = ListNode(2)
    traverse(s.removeZeroSumSublists(head))







if __name__ == "__main__":
    main()
