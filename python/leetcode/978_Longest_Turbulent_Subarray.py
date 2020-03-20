# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = [1 if A[i] > A[i-1] else -1 if A[i] < A[i-1] else 0 for i in range(1, len(A))]
        # print(A)
        ret = 0
        # 用于查找1 0 1 0 1 0 1 0 1 0 序列
        cur = 0
        cur_sum = 0
        # 用于查找-1 0 -1 0 -1 0 -1 0 -1 0 序列
        cur2 = 0
        cur_sum2 = 0
        for num in A:
            if num == 0:
                ret = max(ret, cur+1)
                cur = 0
                cur_sum = 0
                ret = max(ret, cur2+1)
                cur2 = 0
                cur_sum2 = 0
                continue
            if cur_sum + num in [1,0]:
                cur += 1
                cur_sum += num
            else:
                ret = max(ret, cur+1)
                if num in [1, 0]:
                    cur = 1
                    cur_sum = num
                else:
                    cur = 0
                    cur_sum = 0
            if cur_sum2 + num in [-1, 0]:
                cur2 += 1
                cur_sum2 += num
            else:
                ret = max(ret, cur2+1)
                if num in [-1, 0]:
                    cur2 = 1
                    cur_sum2 = num
                else:
                    cur2 = 0
                    cur_sum2 = 0
            # print(cur_sum, cur_sum2)
        return ret


def main():
    s = Solution()
    print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
    print(s.maxTurbulenceSize([1,2,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,1,1]))


if __name__ == "__main__":
    main()
