# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min:
            self.min.append(x)
        else:
            i = 0
            while i < len(self.min):
                if x < self.min[i]:
                    self.min.insert(i, x)
                    break
                i += 1
            if i == len(self.min):
                self.min.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            to_pop = self.stack[-1]
            self.min.remove(to_pop)
            self.stack.pop()
        else:
            pass


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[0]




def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.stack)
    print(minStack.getMin())
    # --> Returns - 3.
    minStack.pop()
    print(minStack.top())
    # --> Returns
    # 0.
    print(minStack.getMin())
    # --> Returns - 2.


if __name__ == "__main__":
    main()
