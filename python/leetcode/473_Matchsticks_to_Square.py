# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):


    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length = int(sum(nums) / 4)
        if length * 4 < sum(nums) or max(nums) > length:
            return False
        nums.sort(reverse=True)
        arr = [0]*4

        def dfs(i):
            if i == len(nums):
                return arr[0] == arr[1] == arr[2] == arr[3]
            for j in range(4):
                if arr[j] + nums[i] <= length:
                    arr[j] += nums[i]
                    if dfs(i+1):
                        return True
                    arr[j] -= nums[i]
            return False

        return dfs(0)


def main():
    s = Solution()
    print(s.makesquare([1,1,2,2,2]))
    print(s.makesquare([3,3,3,3,4]))
    print(s.makesquare([3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]))
    print(s.makesquare([12,12,12,16,20,24,28,32,36,40,44,48,52,56,60]))
    print(s.makesquare([6035753,3826635,922363,6104805,1189018,6365253,364948,2725801,5577769,7857734,2860709,9554210,4883540,8712121,3545089]))


if __name__ == "__main__":
    main()
