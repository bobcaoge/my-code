# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ret = 0
        row = len(A)
        column = len(A[0])
        for j in range(column):
            for i in range(row-1):
                if A[i][j] > A[i+1][j]:
                    ret += 1
                    break
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
