# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def get_length_of_linked_list(self, root):
        """
        :type root: ListNode
        :rtype: int
        """
        length = 0
        while root:
            length += 1
            root = root.next
        return length

    def get_linked_list(self, root, length):
        """

        :type root: ListNode
        :type length: int
        """
        if not root:
            return None, None
        cur = root
        new_root = None
        while cur:
            if length == 1:
                new_root = cur.next
                cur.next = None
                break
            else:
                cur = cur.next
            length -= 1
        return root, new_root

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ret = []
        m, n = divmod(self.get_length_of_linked_list(root), k)
        while k != 0:
            k -= 1
            head, root = self.get_linked_list(root, m + (1 if n > 0 else 0))
            n = n-1 if n > 0 else 0
            ret.append(head)
        return ret


def main():
    s = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    print(s.splitListToParts(root, 1))


if __name__ == "__main__":
    main()
