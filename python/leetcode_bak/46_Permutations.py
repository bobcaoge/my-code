# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = []
    def buffer(self, cur, last):
        """
        :type cur: list[int]
        :type last: list[int]
        :rtype :list[int]
        """
        if not last:
            self.ret.append(cur)
            return
        for index, num in enumerate(last):
            self.buffer(cur+[num], last[:index]+last[index+1:])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self.buffer([], nums)
        return self.ret


def main():
    s = Solution()
    print(s.permute([1,2,3,4]))


if __name__ == "__main__":
    main()
