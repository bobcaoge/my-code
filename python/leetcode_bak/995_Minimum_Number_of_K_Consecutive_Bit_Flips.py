# /usr/bin/python3.6
# -*- coding:utf-8 -*-
# 超时


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        try:
            old_index = A.index(0)
        except:
            return 0
        length = len(A)
        ret = 0
        while old_index <= length - K:
            A[old_index:old_index+K] = [1-x for x in A[old_index:old_index+K]]
            ret += 1
            try:
                old_index = A.index(0)
            except:
                return ret
        # print(A)
        for i in range(length):
            if A[i] == 0:
                return -1
        return ret




def main():
    s = Solution()
    # print(s.minKBitFlips([0,1,0],1))
    print(s.minKBitFlips([1,1,0],2))
    print(s.minKBitFlips(A = [0,0,0,1,0,1,1,0], K = 3))


if __name__ == "__main__":
    main()
