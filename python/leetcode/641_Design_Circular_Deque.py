# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.nums = [0]*k
        self.front = -1
        self.back = -1
        self.size = k
        self.length = 0


    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            if self.isEmpty():
                front = 0
                self.nums[front] = value
                self.back = (self.front+1) % self.size
            else:
                self.front = (self.front-1+self.size) % self.size
                self.nums[self.front] = value
            self.length += 1
            return True
        return False


    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            if self.isEmpty():
                front = 0
                self.nums[front] = value
                self.back = (self.front+1) % self.size
            else:
                self.nums[self.back] = value
                self.back = (self.back+1) % self.size
            self.length += 1
            return True
        return False



    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.length -= 1
            if self.isEmpty():
                self.front = self.back = -1
            else:
                self.front = (self.front+1)%self.size
            return True
        return False


    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.length -= 1
            if self.isEmpty():
                self.front = self.back = -1
            else:
                self.back= (self.back-1+self.size)%self.size
            return True
        return False



    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.nums[self.front]
        return -1


    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.nums[(self.back-1+self.size)%self.size]
        return -1


    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.length == 0


    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.length == self.size



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


def main():
    # s = Solution()
    pass


if __name__ == "__main__":
    main()
