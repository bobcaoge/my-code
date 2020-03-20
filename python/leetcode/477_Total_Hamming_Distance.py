# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = [0]*32
        ones = [0]*32
        for num in nums:
            for i in range(32):
                buff = (num >> i)&1
                zeros[i] += 1-buff
                ones[i] += buff

        ret = 0
        for index, num in enumerate(zeros):
            ret += num*ones[index]
        return ret



def main():
    s = Solution()
    print(s.totalHammingDistance([4,14,2]))


if __name__ == "__main__":
    main()
