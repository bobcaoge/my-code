# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return [num for num in set(nums2) if num in set(nums1)]
        return list(set(nums1) & set(nums2))


def main():
    s = Solution()
    print(s.intersection([1,2,3,4], [2,2]))

if __name__ == "__main__":
    main()
