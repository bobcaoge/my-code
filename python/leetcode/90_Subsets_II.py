# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = [[]]

    def buffer1(self, s, ans):
        if not s:
            return

        for index, num in enumerate(s):
            if index != 0 and num == s[index-1]:
                continue
            self.ret.append(ans+[num])
            self.buffer1(s[index+1:], ans+[num])

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.ret = [[]]
        self.buffer1(nums, [])
        return self.ret


def main():
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))
    print(s.subsetsWithDup([4,4,4,1,4]))


if __name__ == "__main__":
    main()
