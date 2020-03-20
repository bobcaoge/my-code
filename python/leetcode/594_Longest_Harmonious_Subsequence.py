# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findLHS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return 0
        nums.sort()
        nums.append(float('inf'))
        nums = [nums[i] - nums[i-1] for i in range(1, length)]
        print(nums)
        cur_length = 0
        max_length = 0
        queue = []
        length = len(nums)
        for i in range(length):
            # print(cur_length)
            if not queue:
                if nums[i] <= 1:
                    queue.append(nums[i])
                    cur_length += 2
            else:
                if sum(queue) + nums[i] in [0, 1]:
                    queue.insert(0, nums[i])
                    cur_length += 1
                else:
                    if sum(queue) == 1:
                        max_length = max(max_length, cur_length)
                    queue.insert(0, nums[i])
                    while sum(queue) > 1:
                        queue.pop()
                    cur_length = len(queue)+1 if len(queue) > 0 else 0
        if sum(queue) == 1:
            max_length = max(max_length, cur_length)

        return max_length
    def findLHS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return 0
        nums.sort()
        nums = [nums[i] - nums[i-1] for i in range(1, length)]
        # print(nums)
        cur_length = 0
        max_length = 0
        queue = []
        length = len(nums)
        sum_ = 0
        length_of_queue = 0
        for i in range(length):
            if not queue:
                if nums[i] <= 1:
                    queue.append(nums[i])
                    cur_length += 2
                    length_of_queue += 1
                    sum_ += nums[i]
            else:
                if sum_ + nums[i] in [0, 1]:
                    queue.insert(0, nums[i])
                    length_of_queue += 1
                    sum_ += nums[i]
                    cur_length += 1
                else:
                    if sum_ == 1:
                        max_length = max(max_length, cur_length)
                    queue.insert(0, nums[i])
                    length_of_queue += 1
                    sum_ += nums[i]
                    while sum_ > 1:
                        sum_ -= queue.pop()
                        length_of_queue -= 1
                    cur_length = length_of_queue + 1 if length_of_queue else 0
        if sum_ == 1:
            max_length = max(max_length, cur_length)

        return max_length

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        ret = 0
        for num in nums:
            m[num] = m.get(num, 0) + 1
            if m.get(num-1, 0):
                ret = max(ret, m[num]+m[num-1])
            if m.get(num+1, 0):
                ret = max(ret, m[num]+m[num+1])
        return ret


def main():
    s = Solution()
    print(s.findLHS([1,3,2,2,5,2,3,7]))
    print(s.findLHS([1,2,3,4]))
    print(s.findLHS([1,1,1,1]))
    print(s.findLHS([1,2,2,1]))
    print(s.findLHS([1,2,1,3,0,0,2,2,1,3,3]))


if __name__ == "__main__":
    main()
