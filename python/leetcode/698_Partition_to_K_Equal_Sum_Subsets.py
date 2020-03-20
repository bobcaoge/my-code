# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def recursion(self, groups, nums):
        if not nums:
            return True
        v = nums.pop()
        for i in range(len(groups)):
            if groups[i] >= v:
                groups[i] -= v
                if self.recursion(groups, nums):
                    return True
                groups[i] += v
        nums.append(v)
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        target = total / k
        if max(nums) > target:
            return False
        nums.sort()
        if nums and nums[-1] == target:
            k -= 1
            nums.pop()
        return self.recursion([target]*k, nums)


def main():
    s = Solution()
    print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], k = 4))
    # print(s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3))


if __name__ == "__main__":
    main()
