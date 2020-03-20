# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def fairCandySwap1(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = 0
        sum_b = 0
        map_a = {}
        map_b = {}
        for i in A:
            sum_a += i
            map_a[i] = map_a.get(i, 0) + 1
        for i in B:
            sum_b += i
            map_b[i] = map_b.get(i, 0) + 1
        avg = (sum_a + sum_b)/2
        for i in A:
            another = int(avg - (sum_a - i))
            if map_b.get(another, 0) != 0:
                return [i, another]
    def fairCandySwap2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = sum(A)
        sum_b = 0
        map_b = {}
        for i in B:
            sum_b += i
            map_b[i] = map_b.get(i, 0) + 1
        avg = (sum_a + sum_b)/2
        for i in A:
            another = int(avg - (sum_a - i))
            if map_b.get(another, 0) != 0:
                return [i, another]
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = sum(A)
        sum_b = sum(B)
        set_b = set(B)
        avg = (sum_a + sum_b)/2
        for i in A:
            another = int(avg - (sum_a - i))
            if another in set_b:
                return [i, another]

def main():
    s = Solution()
    print(s.fairCandySwap([1,1], [2, 2]))
    print(s.fairCandySwap([1,2], [2, 3]))
    print(s.fairCandySwap([2], [1, 3]))
    print(s.fairCandySwap([1, 2, 5], [2, 4]))

if __name__ == "__main__":
    main()
