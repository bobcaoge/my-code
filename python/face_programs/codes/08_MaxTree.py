# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from data_structure.stack import Stack


class Node(object):
    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self._value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


def pop_stack_set_map(stack, big_map):
    pop_node = stack.pop()
    if stack.is_empty():
        big_map[pop_node] = None
    else:
        big_map[pop_node] = stack.peek()


def get_max_tree(data_list):
    l_big_map = {}
    r_big_map = {}
    stack = Stack()
    node_list = []
    for data in data_list:
        node_list.append(Node(data))

    for cur_node in node_list:
        while (not stack.is_empty()) and stack.peek().get_value() < cur_node.get_value():
            pop_stack_set_map(stack, l_big_map)
        stack.push(cur_node)
    while not stack.is_empty():
        pop_stack_set_map(stack, l_big_map)

    for cur_node in reversed(node_list):
        while (not stack.is_empty()) and stack.peek().get_value() < cur_node.get_value():
            pop_stack_set_map(stack, r_big_map)
        stack.push(cur_node)
    while not stack.is_empty():
        pop_stack_set_map(stack, r_big_map)

    head = None
    for cur_node in node_list:
        left_big = l_big_map[cur_node]
        right_big = r_big_map[cur_node]

        if left_big is None and right_big is None:
            head = cur_node
        elif left_big is None:
            if right_big.left is None:
                right_big.left = cur_node
            else:
                right_big.right = cur_node
        elif right_big is None:
            if left_big.left is None:
                left_big.left = cur_node
            else:
                left_big.right = cur_node
        else:
            big_node = right_big if left_big.get_value() > right_big.get_value() else left_big
            if big_node.left is None:
                big_node.left = cur_node
            else:
                big_node.right = cur_node
    return head


def preorder_traversal(head):
    if head is None:
        return
    print(head.get_value())
    preorder_traversal(head.left)
    preorder_traversal(head.right)


def inorder_traversal(head):
    if head is None:
        return
    inorder_traversal(head.left)
    print(head.get_value())
    inorder_traversal(head.right)


def main():
    data_list = [3, 4, 5, 1, 2]
    head = get_max_tree(data_list)
    preorder_traversal(head)
    print("++++++++++++++")
    inorder_traversal(head)


if __name__ == "__main__":
    main()
