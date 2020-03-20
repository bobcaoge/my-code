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
        if not head or not head.next:
            return head
        before = None

        cur = head.next
        last = head.val
        count = 0
        while cur:
            if cur.val == last:
                count += 1
            else:
                if before is None:
                    if count == 0:
                        before = head
                    else:
                        head = cur
                else:
                    if count == 0:
                        before = before.next
                    else:
                        before.next = cur
                last = cur.val
                count = 0
            cur = cur.next
        return head



def main():
    s = Solution()


if __name__ == "__main__":
    main()
