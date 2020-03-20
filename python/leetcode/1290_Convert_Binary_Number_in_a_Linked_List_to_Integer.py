# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ret = 0
        while head:
            ret = (ret << 1) + head.val
            head = head.next
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
