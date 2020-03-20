# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect


class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        sum_arr = []
        for num in arr:
            if not sum_arr:
                sum_arr.append(num)
            else:
                sum_arr.append(sum_arr[-1]+num)
        length = len(arr)
        ret = 0
        closet_rate = 1<<31
        start = 0
        end = 100000
        mid = (start+end)//2
        while start <= end:
            pos = bisect.bisect(arr, mid)
            diff = target -((sum_arr[pos-1] if pos-1 >= 0 else 0)+(length-pos)*mid)
            abs_diff = abs(diff)
            if abs_diff < closet_rate:
                ret = mid
                closet_rate = abs_diff
            elif abs_diff == closet_rate:
                ret = min(ret, mid)
            if diff > 0:
                start = mid+1
            else:
                end = mid-1
            mid = (start+end)//2
        return ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
