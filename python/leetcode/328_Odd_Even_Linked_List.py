# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return head
        odd = None
        even = None
        flag = True
        ret = None
        even_head = None
        while head:
            cur = head
            head = head.next
            cur.next = None
            if flag:
                if odd is None:
                    odd = cur
                    ret = cur
                else:
                    odd.next = cur
                    odd = cur
                flag = False
            else:
                if even is None:
                    even_head= cur
                    even = cur
                else:
                    even.next = cur
                    even = cur
                flag = True
        odd.next = even_head
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
