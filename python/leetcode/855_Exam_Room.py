# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq

class ExamRoom(object):

    def get_distance(self, distance):
        return - ((distance >> 1) << 1)

    def __init__(self, N):
        """
        :type N: int
        """
        self.length = N
        self.heap= [[-(4*N-4),-(2*N-2), 2*N-2]]
        self.keep = {}

    # def add_closet(self,a):
    def add(self, left, right):
        if left < 0:
            left = -right
        elif right > self.length:
            right = 2*(self.length-1)-left
        distance = self.get_distance(right-left)
        mid = (right + left)//2
        if 0<= mid < self.length and right > left:
            heapq.heappush(self.heap, [distance, left, right])
            self.add_closet(left, right, 1)
            self.add_closet(right, left, 0)

    def add_closet(self, a, closet, left):
        if 0 <= a < self.length:
            if not self.keep.get(a, None):
                self.keep[a] = [0, 0]
            self.keep[a][left] = closet

    def remove(self, left, right):
        distance = self.get_distance(right-left)
        try:
            self.heap.remove([distance, left, right])
            heapq.heapify(self.heap)
        except:
            pass

    def seat(self):
        """
        :rtype: int
        """
        if self.length == 1:
            return 0
        distance, left, right = heapq.heappop(self.heap)
        mid = int((right+left)/2)
        self.add(left, mid)
        self.add(mid, right)
        return mid

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        if self.length == 1:
            return
        left, right = self.keep[p]
        if p == 0:
            left = -right
        if p == self.length-1:
            right = 2*(self.length-1) - left
        self.add(left, right)
        self.remove(left, p)
        self.remove(p, right)


def main():
    s = ExamRoom(10)
    print(s.heap)
    print(s.keep)
    print(s.seat())
    print(s.heap)
    print(s.keep)
    print(s.seat())
    print(s.heap)
    print(s.keep)
    print(s.leave(9))
    print(s.keep)
    print(s.seat())



if __name__ == "__main__":
    main()
