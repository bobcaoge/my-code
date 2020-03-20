# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import copy


class Node(object):
    def __init__(self, value):
        self._value = value
        self.next = None


class LinkList(object):
    """
    头结点不包含数据的链表
    """
    def __init__(self, head=None):
        if head is None:
            self._head = self.create()
        else:
            self._head = head

    def insert(self, data, place=None):
        if place is None:
            node = Node(data)
            node.next = self._head.next
            self._head.next = node

    def poll_last(self):
        head = copy.deepcopy(self._head)
        if head.next is None:
            return
        before = head
        head = head.next
        while not head.next:
            before = head
            head.next = head.next.next
        before.next = None

    def create(self):
        self._head = Node(None)


def main():
    pass


if __name__ == "__main__":
    main()
