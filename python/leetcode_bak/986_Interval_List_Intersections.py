# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        index_a = 0
        index_b = 0
        ret = []
        while index_b < len(B) and index_a < len(A):
            a = A[index_a] # tuple (start, end)
            b = B[index_b]
            if b.start < a.start:
                if b.end < a.start:
                    index_b += 1
                elif b.end < a.end:
                    ret.append(Interval(a.start, b.end))
                    index_b += 1
                else:
                    ret.append(a)
                    index_a += 1
            elif b.start <= a.end:
                if b.end <= a.end:
                    ret.append(b)
                    index_b += 1
                else:
                    ret.append(Interval(b.start, a.end))
                    index_a += 1
            else:
                index_a += 1
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
