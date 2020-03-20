# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from random import randint


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head



    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cur = self.head
        ret = cur
        i = 1
        # 第一个数已知，从第二个数开始计算概率， 1/i 的概率重置
        while cur.next:
            if randint(1, i+1) == i:
                ret = cur.next
            cur = cur.next
            i += 1
        return ret.val



def main():
    s = Solution(None)


if __name__ == "__main__":
    main()
