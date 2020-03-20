# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2
        while start <= end:
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] == nums[start]:
                flag = True
                for i in range(start+1, mid):
                    if nums[i] != nums[i-1]:
                        flag = False
                        break
                if flag:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            mid = (start + end) / 2

        return False




def main():
    s = Solution()
    print(s.search([1,3,1,1,1], 3))


if __name__ == "__main__":
    main()
