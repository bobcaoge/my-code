# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_A = sum(A)
        last_fk = 0
        for i, num in enumerate(A):
            last_fk += num * i
        ret = last_fk
        for i in range(len(A)-1, 0, -1):
            fk = last_fk + sum_A - len(A)*A[i]
            ret = max(ret, fk)
            last_fk = fk
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
