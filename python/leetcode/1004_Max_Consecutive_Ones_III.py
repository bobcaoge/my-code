# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        before = 0
        ret = 0
        flipped = 0
        for i, num in enumerate(A):
            if num == 0:
                flipped += 1
                while flipped > K:
                    flipped -= 1 - A[before]
                    before += 1
            ret = max(ret, i-before+1)
        return ret


def main():
    s = Solution()
    print(s.longestOnes( A = [1,1,1,0,0,0,1,1,1,1,0], K = 2))
    print(s.longestOnes(A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3))


if __name__ == "__main__":
    main()
