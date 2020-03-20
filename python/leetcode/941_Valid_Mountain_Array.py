# /usr/bin/python3.6
# -*- coding:utf-8 -*-



class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        chang_flag = False
        length = len(A)
        if length < 3:
            return False
        for i in range(length-1):
            if A[i] == A[i+1]:
                return False
            if not chang_flag:
                if A[i] > A[i+1]:
                    if i == 0:
                        return False
                    chang_flag = True
            if chang_flag:
                if A[i] < A[i+1]:
                    return False
        return chang_flag


def main():
    s = Solution()


if __name__ == "__main__":
    main()
