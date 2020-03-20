# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(i-A[i]) > 1:
                return False
        return True


def main():
    s = Solution()
    print(s.isIdealPermutation([1,0,2]))
    print(s.isIdealPermutation([1,2,0]))


if __name__ == "__main__":
    main()
