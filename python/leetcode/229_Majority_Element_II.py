# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        return [key for key, value in m.items() if value >= len(nums)/3]
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        candidateA  = nums[0]
        candidateB = nums[0]
        countA = 0
        countB = 0
        for num in nums:
            if num == candidateA:
                countA += 1
                continue
            if num == candidateB:
                countB += 1
                continue
            if countA == 0:
                candidateA = num
                countA += 1
                continue
            if countB == 0:
                candidateB = num
                countB += 1
                continue
            countA -= 1
            countB -= 1

        countA = countB = 0
        for num in nums:
            if num == candidateA:
                countA += 1
            elif num == candidateB:
                countB += 1
        ret = []
        if countB > len(nums)/3:
            ret.append(candidateB)
        if countA > len(nums)/3:
            ret.append(candidateA)
        return ret




def main():
    s = Solution()
    # print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9]))


if __name__ == "__main__":
    main()
