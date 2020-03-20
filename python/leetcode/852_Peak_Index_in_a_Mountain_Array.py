# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for index, num in enumerate(A[:-1]):
            if num > A[index+1]:
                return index



def main():
    s = Solution()


if __name__ == "__main__":
    main()
