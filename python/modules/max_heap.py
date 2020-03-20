# coding:utf-8

"""
有哨兵的最大堆
"""
class MaxHeap:
    def __init__(self):
        self.size = 0
        self.nums = [2**32]

    def push(self, num):
        if self.size+1 < len(self.nums):
            self.nums[self.size+1] = num
        else:
            self.nums.append(num)
        self.size += 1
        cur = self.size
        while self.nums[cur] > self.nums[cur/2]:
            self.nums[cur], self.nums[cur/2] = self.nums[cur/2], self.nums[cur]
            cur = cur/2

    def pop(self):
        if self.size == 0:
            return
        ret = self.nums[1]
        self.nums[1] = self.nums[self.size]
        self.size -= 1
        cur = 1
        while cur*2 <= self.size:
            child = cur * 2
            if child+1 <= self.size and self.nums[child+1] > self.nums[child]:
                child += 1
            if self.nums[cur] >= self.nums[child]:
                break
            self.nums[cur], self.nums[child] = self.nums[child], self.nums[cur]
            cur = child
        # self.nums.pop()
        return ret


def main():
    heap = MaxHeap()
    for i in range(10):
        heap.push(i)
        print heap.nums
    for i in range(10):
        print(heap.pop())
        print heap.nums


if __name__ == '__main__':
    main()
