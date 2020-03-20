# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if 0 <= index <= len(self.nums):
            return self.nums[index]
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.nums.insert(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.nums.append(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if 0 <= index < len(self.nums):
            self.nums.insert(index, val)
        elif index == len(self.nums):
            self.nums.append(val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if 0 <= index < len(self.nums):
            self.nums = self.nums[:index] + self.nums[index+1:]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
