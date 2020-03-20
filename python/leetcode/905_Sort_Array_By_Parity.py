# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(A) - 1
        while start < end:
            if A[start] % 2 == 1 and A[end] % 2 == 0:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            if A[start] % 2 == 0:
                start += 1
            if A[end] % 2 == 1:
                end -= 1
        return A

def main():
    s = Solution()


if __name__ == "__main__":
    main()
