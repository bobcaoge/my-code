# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s = []
        while head:
            s.append(head)
            head = head.next
            s[-1].next = None
        start = 0
        end = len(s)-1
        last = None
        while start <= end:
            if start != end:
                s[start].next = s[end]

            if last :
                last.next = s[start]
            last = s[end]
            end -= 1
            start += 1



def main():
    s = Solution()


if __name__ == "__main__":
    main()
