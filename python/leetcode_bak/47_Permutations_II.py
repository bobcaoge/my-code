# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = []
    s = set()

    def buffer1(self, cur, last):
        """
        :type cur: list[int]
        :type last: list[int]
        :rtype :list[int]
        """
        if not last:
            t_cur = tuple(cur)
            if t_cur not in self.s:
                self.ret.append(cur)
                self.s.add(t_cur)
            return
        for index, num in enumerate(last):
            self.buffer(cur+[num], last[:index]+last[index+1:])

    def buffer(self, cur, last):
        """
        :type cur: list[int]
        :type last: list[int]
        :rtype :list[int]
        """
        if not last:
            self.ret.append(cur)
            return
        s = set()
        for index, num in enumerate(last):
            if num not in s:
                self.buffer(cur + [num], last[:index] + last[index + 1:])
                s.add(num)


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self.s = set()
        self.buffer([], nums)
        return self.ret


def main():
    s = Solution()
    print(s.permuteUnique([1,1,2]))


if __name__ == "__main__":
    main()
