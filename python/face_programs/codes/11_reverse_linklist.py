# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode(object):
    def __init__(self, value):
        self.value = value
        self.pre = None
        self.next = None


def reverse_single_linklist(head):
    """
    翻转没有空头结点的链表
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head
    if head.next.next is None:
        after = head.next
        after.next = head
        head.next = None
    before = head
    cur = head.next
    after = cur.next
    before.next = None
    head = None
    while after.next is not None:
        before.next = head
        cur.next = before
        head = before
        before = cur
        cur = after
        after = after.next
    cur.next = before
    after.next = cur
    return after


def reverse_double_direction_linklist(head_p):
    head = head_p
    if head is None or head.next is None:
        return head
    if head.next.next is None:
        after = head.next
        head.next = None
        after.next = head
        head.pre = after
        after.pre = None
        return after
    before = head
    cur = head.next
    after = cur.next
    before.next = None
    head = None
    while after.next is not None:
        before.next = head
        cur.next = before

        if head is not None:
            head.pre = before
        before.pre = cur

        head = before
        before = cur
        cur = after
        after = after.next

    cur.next = before
    after.next = cur

    cur.pre = after
    before.pre = cur
    after.pre = None
    return after, head_p


def traversal_linklist(head):
    """
    遍历没有空头结点的链表
    :param head:
    :return:
    """
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()


def traversal_double_linklist(head, tail):
    """
    遍历没有空头结点的双向链表
    :type tail:
    :param head:
    :return:
    """
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()
    while tail is not None:
        print(tail.value, end=" ")
        tail = tail.pre
    print()


def reverse_part_of_linklist(head, start, end):
    """
    反转链表从start到end的部分
    :param head:
    :param start:
    :param end:
    :return:
    """
    if start < 1 or end - start < 2 or head is None or head.next is None:
        return head
    place = 1
    cur = head
    # 查找start节点
    while place < start - 1 and cur.next is not None:
        cur = cur.next
        place += 1

    place += 1
    if cur is None or cur.next is None:
        return head

    if start == 1:
        end -= 1

    node_before_reversed_linklist = cur
    before = cur.next
    before_keep = before
    cur = before.next
    if cur is None:
        return head
    after = cur.next

    while place < end and after.next is not None:
        cur.next = before
        before = cur
        cur = after
        after = after.next
        place += 1

    head_reversed = before_keep
    flag_reversed_to_tail = False
    node_after_reversed_linklist = None

    if place == end :
            tail_reversed = before
            node_after_reversed_linklist = cur
    elif end - place == 1:
            cur.next = before
            tail_reversed = cur
            node_after_reversed_linklist = after
    else:
            cur.next = before
            after.next = cur
            tail_reversed = after
            flag_reversed_to_tail = True

    if start == 1:
        head_reversed.next = head
        if flag_reversed_to_tail:
            head.next = None
            head = tail_reversed
        else:
            head.next = node_after_reversed_linklist
            head = tail_reversed
    else:
        node_before_reversed_linklist.next = tail_reversed
        if flag_reversed_to_tail:
            head_reversed.next = None
        else:
            node_before_reversed_linklist.next = tail_reversed
            head_reversed.next = node_after_reversed_linklist

    return head


def main_1():
    head = None
    cur = None
    for i in range(10):
        if head is None:
            head = Node(i)
            cur = head
        else:
            cur.next = Node(i)
            cur = cur.next
    traversal_linklist(head)
    traversal_linklist(head)
    print()
    print("*"*10)
    # traversal_linklist(reverse_single_linklist(head))


def main_2():
    head = None
    cur = None
    for i in range(10):
        if head is None:
            head = DoubleNode(i)
            cur = head
        else:
            next_node = Node(i)
            next_node.pre = cur
            cur.next = next_node
            cur = cur.next
    tail = cur
    traversal_double_linklist(head, tail)
    print("*"*10)
    head, tail = reverse_double_direction_linklist(head)
    traversal_double_linklist(head, tail)

    head = tail = DoubleNode(5)
    traversal_double_linklist(head, tail)
    tail = DoubleNode(4)
    head.next = tail
    tail.pre = head
    traversal_double_linklist(head, tail)


def main():
    head = None
    cur = None
    for i in range(1, 11):
        if head is None:
            head = Node(i)
            cur = head
        else:
            cur.next = Node(i)
            cur = cur.next
    traversal_linklist(head)
    print()
    print("*"*10)
    traversal_linklist(reverse_part_of_linklist(head, 3, 10))


if __name__ == "__main__":
    main()
