# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_length_of_linked_list(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        if not head:
            return 0
        s = set(G)

        ret = 1
        while head.next:
            if head.val not in s:
                ret -= 1
            else:
                if head.next.val in s:
                    ret -= 1
            head = head.next
            ret += 1

        if head and head.val not in s:
            ret -= 1
        return ret

def main():
    s = Solution()


if __name__ == "__main__":
    main()
