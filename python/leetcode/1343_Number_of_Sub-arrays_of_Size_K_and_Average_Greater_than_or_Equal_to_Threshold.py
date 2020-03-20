# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        threshold = k*threshold
        sum_of_sub_arr = 0
        for i in range(k-1):
            sum_of_sub_arr += arr[i]
        ret = 0
        for i in range(k-1, len(arr)):
            sum_of_sub_arr += arr[i]
            sum_of_sub_arr -= arr[i-k] if i-k >= 0 else 0
            if sum_of_sub_arr >= threshold:
                ret += 1
        return ret


def main():
    s = Solution()
    print(s.numOfSubarrays( arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
    print(s.numOfSubarrays(arr = [1,1,1,1,1], k = 1, threshold = 0))
    print(s.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))


if __name__ == "__main__":
    main()
