# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        mid = int((start+end)/2)
        while start < end:
            if nums[mid] == nums[mid+1]:
                if (mid - start + 1) % 2 == 0:
                    end = mid - 1
                else:
                    start = mid + 2
            else:
                if (mid - start + 1) % 2 == 0:
                    start = mid + 1
                else:
                    end = mid
            mid = int((start+end)/2)
        return nums[start]



def main():
    s = Solution()
    print(s.singleNonDuplicate([1,1,2,3,3,4,4]))
    print(s.singleNonDuplicate([1,1,2,2,3,3,8,4,4]))
    print(s.singleNonDuplicate([1,3,3,4,4]))
    print(s.singleNonDuplicate([1,3,3]))
    print(s.singleNonDuplicate([3,3,1]))
    print(s.singleNonDuplicate([1,1,2,3,3]))


if __name__ == "__main__":
    main()
