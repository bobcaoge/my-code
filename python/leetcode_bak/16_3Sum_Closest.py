# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closet = 2**32
        ret = 0
        for i in range(length):
            last_j = "A"
            for j in range(i+1, length):
                if last_j == nums[j]:
                    continue
                else:
                    last_j = nums[j]
                buff = nums[i] + nums[j]
                last = "a"
                cur = 2**32
                for k in range(j+1, length):
                    if nums[k] == last:
                        continue
                    else:
                        last = nums[k]
                    bu = abs(buff + nums[k] - target)
                    if bu > cur:
                        break
                    else:
                        if bu < closet:
                            ret = buff+nums[k]
                            closet = bu
                        cur = bu
        return ret




def main():
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([0,0,0], 1))
    print(s.threeSumClosest([1,1,1,0], -100))


if __name__ == "__main__":
    main()
