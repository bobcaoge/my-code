# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = int((start + end) / 2)
        while start <= end:
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            mid = int((start + end) / 2)
        return -1




    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = int((start + end) / 2)
        while start <= end:
            if nums[mid] == target:
                return mid
            # 中间有断点
            if nums[start] >= nums[end]:
                if nums[mid] >= nums[start] :
                    if nums[mid] > target >= nums[start]:
                        end = mid - 1
                        mid = int((start + end) / 2)
                    else:
                        start = mid + 1
                        mid = int((start + end) / 2)
                else:
                    if nums[mid] < target <= nums[end]:
                        start = mid + 1
                        mid = int((start + end) / 2)
                    else:
                        end = mid - 1
                        mid = int((start + end) / 2)


            # 中间无断点， 正序
            elif nums[start] <= nums[mid] <= nums[end]:
                if target > nums[mid]:
                    start = mid + 1
                    mid = int((start + end) / 2)
                else:
                    end = mid - 1
                    mid = int((start + end) / 2)
            # 中间无断点， 逆序
            elif nums[start] >= nums[mid] >= nums[end]:
                if target > nums[mid]:
                    end = mid - 1
                    mid = int((start + end) / 2)
                else:
                    start = mid + 1
                    mid = int((start + end) / 2)
            else:
                break
        return -1





def main():
    s = Solution()
    nums = [4,5,6,7,8,1,2,3]
    for num in nums:
        print(s.search(nums, num))
    print(s.search(nums, 9))


if __name__ == "__main__":
    main()
