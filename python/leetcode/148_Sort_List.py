# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def emerge(self, node_list, start, end):
        if start == end:
            return [node_list[start]]
        else:
            mid = (start+end)/2
            left = self.emerge(node_list, start, mid)
            right = self.emerge(node_list, mid+1, end)
            buff = []
            index_of_left = 0
            index_of_right = 0
            while index_of_left < len(left) and index_of_right< len(right):
                if left[index_of_left].val <= right[index_of_right].val:
                    buff.append(left[index_of_left])
                    index_of_left += 1
                else:
                    buff.append(right[index_of_right])
                    index_of_right += 1
            if index_of_right < len(right):
                buff.extend(right[index_of_right:])
            if index_of_left < len(left):
                buff.extend(left[index_of_left:])
            # print(buff)
            return buff

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        s = []
        while head:
            s.append(head)
            head = head.next
            s[-1].next = None
        node_list = self.emerge(s, 0, len(s)-1)
        head = node_list[0]
        for i in range(len(s)-1):
            node_list[i].next = node_list[i+1]
        return head





def main():
    s = Solution()


if __name__ == "__main__":
    main()
