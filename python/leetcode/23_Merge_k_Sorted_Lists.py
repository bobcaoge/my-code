# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Heap(object):
    def __init__(self, size=-1):
        self.size = 10 if size < 0 else size
        self.heap = [None]*self.size
        self.length = 0

    def push(self, node):
        if self.length == self.size:
            return False
        pos = self.length
        self.length += 1
        child = int((pos+1)/2-1)
        while pos != 0 and node.val < self.heap[child].val:
            self.heap[pos] = self.heap[child]
            pos = child
            child = int((pos+1)/2-1)
        self.heap[pos] = node

    def pop(self):
        if self.length == 0:
            return None
        ret = self.heap[0]
        parent = 0
        self.heap[0] = self.heap[self.length-1]
        left = (parent+1)*2-1
        right = (parent+1)*2
        self.length -= 1
        while left < self.length:
            index = parent
            if self.heap[left].val < self.heap[parent].val:
                index = left
            if right < self.length and self.heap[right].val < self.heap[left].val and self.heap[right].val < self.heap[parent].val:
                index = right
            if index == parent:
                break
            else:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                parent = index
                left = (parent+1)*2-1
                right = (parent+1)*2
        return ret



class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = Heap(len(lists))
        for node in lists:
            if node:
                heap.push(node)
        head = ListNode(0)
        cur = head
        while heap.length > 0:
            node = heap.pop()
            if node.next:
                heap.push(node.next)
            cur.next = node
            cur = node
        return head.next


def main():
    s = Solution()


if __name__ == "__main__":
    main()
