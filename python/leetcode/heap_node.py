#! /usr/bin/python3.6
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
        parent = int((pos+1)/2-1)
        while pos != 0 and node.val < self.heap[parent].val:
            self.heap[pos] = self.heap[parent]
            pos = parent
            parent = int((pos+1)/2-1)
        self.heap[pos] = node

    def pop(self):
        if self.length == 0:
            return None
        ret = self.heap[0]
        parent = 0
        self.heap[0] = self.heap[self.length-1]
        self.length -= 1

        left = (parent+1)*2-1
        right = (parent+1)*2
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

    def print(self):
        for i in range(self.length):
            print(self.heap[i].val, end=" ")
        print()


def main():
    heap = Heap(10)
    for i in range(10):
        heap.push(ListNode(10-i))
        heap.print()
    for i in range(10):
        print(heap.pop().val)
        heap.print()



if __name__ == "__main__":
    main()