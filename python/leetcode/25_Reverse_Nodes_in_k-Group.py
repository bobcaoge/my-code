# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        def reverse(left, end):
            tail = left
            before = None
            cur = left
            after = left.next
            while after != end:
                cur.next = before
                before, cur, after = cur, after, after.next
            cur.next = before
            return cur, tail
        prehead = ListNode(0)
        prehead.next = head
        i = 0
        ret = prehead
        cur = head
        while cur:
            cur = cur.next
            i += 1
            if i == k:
                l, r = reverse(prehead.next, cur)
                prehead.next = l
                r.next = cur
                prehead = r
                i = 0
        return ret.next


def main():
    s = Solution()
    prehead = ListNode(0)
    cur = prehead
    for num in [1,2,3,4,5]:
        cur.next = ListNode(num)
        cur = cur.next
    ret = s.reverseKGroup(prehead.next, 2)
    print()



if __name__ == "__main__":
    main()
