# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = False
        # index_of_min_num = len(nums) - 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                # print(i)
                index_of_min_num = i
                for j in range(i, len(nums)):
                    if nums[index_of_min_num] > nums[j] > nums[i-1]:
                        index_of_min_num = j
                nums[i-1], nums[index_of_min_num] = nums[index_of_min_num], nums[i-1]
                nums[i:] = sorted(nums[i:])
                flag = True
                break
            # if nums[i] < nums[index_of_min_num]:
            #     index_of_min_num = i
        if not flag:
            # print("===")
            nums.sort()



def main():
    s = Solution()
    nums = [1,3,2]
    s.nextPermutation(nums)
    print(nums)
    nums = [2,3,1]
    s.nextPermutation(nums)
    print(nums)


if __name__ == "__main__":
    main()
