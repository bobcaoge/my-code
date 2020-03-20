# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ret = 0
        length_of_word = len(A[0])
        length_of_A = len(A)
        is_sorted = [0]*(length_of_A-1)
        for j in range(length_of_word):
            is_sorted2 = is_sorted[:]
            for i in range(length_of_A-1):
                if A[i][j] > A[i+1][j] and is_sorted[i] == 0:
                    ret += 1
                    break
                is_sorted2[i] |= A[i][j] < A[i+1][j]
            else:
                is_sorted = is_sorted2
        return ret

    def minDeletionSize2(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = [list(x) for x in A]

        def indexes(a, b):
            s = set()
            for i in range(len(a)):
                if a[i] > b[i]:
                    s.add(i)
                    break
                if a[i] < b[i]:
                    break
            return s

        def get_delete_indexes():
            s = set()
            for i in range(len(A)-1):
                s.update(indexes(A[i], A[i+1]))
            return s
        ret = 0
        while True and len(A[0]) > 0:
            s = get_delete_indexes()
            ret += len(s)
            if len(s) == 0:
                return ret

            for row in A:
                for i, col in enumerate(sorted(s)):
                    row.pop(col-i)
            # print(A)
        return ret


def main():
    s = Solution()
    print(s.minDeletionSize(["ca","bb","ac"]))
    print(s.minDeletionSize(["xga","xfb","yfa"]))
    print(s.minDeletionSize(["abx","agz","bgc","bfc"]))


if __name__ == "__main__":
    main()
