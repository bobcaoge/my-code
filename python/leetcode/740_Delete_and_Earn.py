# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for num in nums:
            m[num] = m.get(num, 0)+1

        info = sorted([[num, count] for num, count in m.items()])
        old_delete = info[0][0]*info[0][1]
        old_not_delete = 0
        old_num = info[0][0]
        for num, count in info[1:]:
            if num != old_num+1:
                cur_delete = max(old_not_delete, old_delete)+num*count
            else:
                cur_delete = old_not_delete + num*count
            cur_not_delete = max(old_not_delete, old_delete)
            old_delete, old_not_delete = cur_delete, cur_not_delete
            old_num = num
        return max(old_not_delete, old_delete)

    def deleteAndEarn1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                if nums[j] != nums[i]-1:
                    dp[i] = max(dp[i], dp[j]+nums[i])
        return max(dp)


def main():
    s = Solution()
    print([x for x in range(22)])
    print(s.deleteAndEarn([2,3,4]))
    print(s.deleteAndEarn([2,2,3,3,3,4]))
    print(s.deleteAndEarn([1,3,2,6,4,7,4,7,98,54,3,6,3,2,2,6,7,8,4,3,2,3,45,6,7,7,7,7,4,4,4,4]))
    print(s.deleteAndEarn([x for x in range(22)]))


if __name__ == "__main__":
    main()
