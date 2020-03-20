# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        min_num = 100000
        for i in range(len(A)-1, -1, -1):
            if min_num < A[i]:
                pos = -1
                num = -1
                for j in range(i+1, len(A)):
                    if num < A[j] < A[i]:
                        pos = j
                        num = A[j]
                A[i], A[pos] = A[pos], A[i]
                return A
            min_num = min(min_num, A[i])
        return A


def main():
    s = Solution()
    print(s.prevPermOpt1([3,2,1]))
    print(s.prevPermOpt1([1,1,5]))
    print(s.prevPermOpt1([1,9,4,6,7]))
    print(s.prevPermOpt1([3,1,1,3]))


if __name__ == "__main__":
    main()
