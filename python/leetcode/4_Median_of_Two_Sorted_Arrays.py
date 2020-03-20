# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1+nums2)
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[len(nums)//2-1])/2
        return nums[len(nums)//2]




def main():
    s = Solution()
    # nums1 = [3]
    # nums2 = [-2,-1]
    nums2 = [2,4,6,8]
    nums1 = [1,3,5,7,9]
    ret = s.findMedianSortedArrays(nums1,nums2)
    print(ret)


if __name__ == "__main__":
    main()
