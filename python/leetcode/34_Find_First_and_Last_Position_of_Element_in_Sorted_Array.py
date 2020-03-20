# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        mid = int((start+end)/2)
        flag = -1
        ret = []
        while start <= end:
            if nums[mid] == target:
                flag = mid
                break
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
            mid = int((start+end)/2)
        if flag == -1:
            return [-1,-1]
        # print("===")
        # get left position
        start = 0
        end = flag
        mid = int((start+end)/2)
        while start < end:
            if nums[start] == target:
                break
            if nums[mid] == target:
                end = mid
            else:
                start = mid + 1
            mid = int((start+end)/2)
        ret.append(start)

        # print("===")
        # get right position
        start = flag
        end = len(nums)-1
        mid = int((start+end)/2)
        while start != mid:
            if nums[end] == target:
                start = end
                break
            if nums[mid] == target:
                start = mid
            else:
                end = mid - 1
            mid = int((start+end)/2)
        if nums[end] == target:
            ret.append(end)
        else:
            ret.append(start)

        return ret


def main():
    s = Solution()
    print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
    print(s.searchRange(nums = [1,2,2], target = 2))

if __name__ == "__main__":
    main()
