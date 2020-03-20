# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten_helper(self, head):
        """
        :type head: Node
        :return:
        """
        cur = head

        while True:
            if cur.child is None and cur.next is None:
                return head, cur
            if cur.child:
                h, t = self.flatten_helper(cur.child)
                cur.child = None
                t.next = cur.next
                cur.next = h
                h.prev = cur
                if t.next:
                    t.next.prev = t
                    cur = t.next
                else:
                    cur = t
            else:
                cur = cur.next

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        return self.flatten_helper(head)[0]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
