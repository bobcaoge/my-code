# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        mod = 10**9+7
        dp1 = [0]*len(arr) # left to right
        dp1[0] = arr[0]
        for i in range(1, len(arr)):
            dp1[i] = max(dp1[i-1]+arr[i], arr[i])

        dp2 = [0]*len(arr) # left to right
        dp2[-1] = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            dp2[i] = max(dp2[i+1]+arr[i], arr[i])
        ret = 0
        ret = max(max(dp1), ret)
        if k == 1:
            return ret
        sum_of_arr = sum(arr)
        if sum_of_arr > 0:
            return max(ret, dp2[0]+dp1[-1], dp2[0]+sum_of_arr*(k-2)%mod+dp1[-1])%mod
        return max(ret, dp2[0]+dp1[-1])


def main():
    s = Solution()
    print(s.kConcatenationMaxSum(arr = [1,2], k = 3))
    print(s.kConcatenationMaxSum(arr = [1,-2,1], k = 5))
    print(s.kConcatenationMaxSum(arr = [-1,-2], k = 7))


if __name__ == "__main__":
    main()
