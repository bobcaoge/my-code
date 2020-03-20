# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        to_check = {A[0], B[0]}
        ret = 1<<31
        for flag in to_check:
            nums_in_A = 0
            nums_in_B = 0
            for i, num in enumerate(A):
                if A[i] != flag and B[i] != flag:
                    break
                if A[i] == flag:
                    nums_in_A += 1
                if B[i] == flag:
                    nums_in_B += 1
            else:
                ret = min(ret, len(A)-nums_in_A, len(A)-nums_in_B)
        return ret if ret != 1<<31 else -1






def main():
    s = Solution()


if __name__ == "__main__":
    main()
