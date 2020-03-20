# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        return [x[1] for x in sorted([[value, key] for key, value in m.items()])[::-1][:k]]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
