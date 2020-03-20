# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def ascend(self, arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def decrease(self, arr):
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
        return True
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return self.ascend(A) or self.decrease(A)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
