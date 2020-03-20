# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1.sort()
        # nums2.sort()
        length1 = len(nums1)
        length2 = len(nums2)
        short_length, short_nums, long_nums = (length1, nums1, nums2) if length1 <= length2 else (length2,nums2,nums1)
        ret = []
        for num in short_nums:
            if num in long_nums:
                ret.append(num)
                long_nums.remove(num)

        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
