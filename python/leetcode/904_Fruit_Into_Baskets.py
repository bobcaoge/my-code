# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        ret = 0
        nums = collections.Counter()
        i = 0
        j = 0
        while j < len(tree):
            nums[tree[j]] += 1
            while len(nums) > 2:
                nums[tree[i]] -= 1
                if nums[tree[i]] == 0:
                    del nums[tree[i]]
                i += 1
            ret = max(ret, j-i+1)
            j += 1

        return max(ret, j-i)


def main():
    s = Solution()
    print(s.totalFruit([1,2,2]))
    print(s.totalFruit([0,1,2,2]))
    print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))


if __name__ == "__main__":
    main()
