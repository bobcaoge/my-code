# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        A.append(2**32)
        last = 0
        ret = 0
        old = 2**32
        for i in range(len(A)-1):
            if A[i+1]-A[i] == old:
                last += 1
            else:
                old = A[i+1] - A[i]
                if last > 1:
                    last -= 1
                    ret += last*(last+1)/2
                last = 1
        return ret

    def numberOfArithmeticSlices1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        diffs = [A[i+1] - A[i] for i in range(len(A)-1)]
        diffs.append(2**32)
        print(diffs)

        ret = 0
        last = 1
        for i in range(1, len(diffs)):
            if diffs[i] == diffs[i-1]:
                last += 1
            else:
                if last > 1:
                    last -= 1
                    ret += last*(last+1)/2
                last = 1
        return ret

def main():
    s = Solution()
    print(s.numberOfArithmeticSlices([1,2,3,4,5, 1,2,3,4,5]))
    print(s.numberOfArithmeticSlices([1,2,3]))


if __name__ == "__main__":
    main()
