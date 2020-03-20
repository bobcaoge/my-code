# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        intervals = [0]*len(A)
        ret = 0
        flip = 0
        for i, num in enumerate(A):
            flip += intervals[i] # 当前位置翻转的次数
            num = num if flip % 2 == 0 else 1 - num
            if num == 0:
                ret += 1
                if i + K > len(A):
                    return -1
                if i+K < len(A):
                    intervals[i+K] += 1
                flip += 1

        return ret


def main():
    s = Solution()
    print(s.minKBitFlips( A = [0,1,0], K = 1))
    print(s.minKBitFlips(A = [0,0,0,1,0,1,1,0], K = 3))


if __name__ == "__main__":
    main()
