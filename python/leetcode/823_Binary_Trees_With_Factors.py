# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        s = set(A)
        m = {}
        ret = 0
        for i, num in enumerate(A):
            cur = 1
            for j in range(i):
                if num % A[j] == 0 and num / A[j] in s:
                    cur += m[A[j]]*m[num/A[j]] % 1000000007
            m[num] = cur
            ret += cur
        return ret % 1000000007


def main():
    s = Solution()
    # print(s.numFactoredBinaryTrees([2,4]))
    print(s.numFactoredBinaryTrees(A = [2, 4, 5, 10]))
    print(s.numFactoredBinaryTrees([2,4,8,16,32,64,128]))


if __name__ == "__main__":
    main()
