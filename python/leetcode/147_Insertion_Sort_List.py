# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = head
        while head:
            cur = head.next
            min_node = head
            while cur:
                if min_node.val > cur.val:
                    min_node = cur
                cur = cur.next

            if min_node != head:
                min_node.val, head.val = head.val, min_node.val
            head = head.next
        return ret

    def insertionSortList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
            node_list[-1].next = None
        length = len(node_list)
        for i in range(length):
            for j in range(i+1, length):
                if node_list[i].val > node_list[j].val:
                    node_list[i], node_list[j] = node_list[j], node_list[i]
        for i in range(length-1):
            node_list[i].next = node_list[i+1]
        return node_list[0] if node_list else head




def main():
    s = Solution()


if __name__ == "__main__":
    main()
