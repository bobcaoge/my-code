# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):

    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = collections.Counter(nums)
        arr = sorted(set(nums))
        while arr:
            start = 0
            stack = []
            for num in arr:
                if not stack:
                    stack.append(num)
                    m[num] -= 1
                else:
                    if num - stack[-1] > 1:
                        break
                    if m[num] > m[stack[-1]]:
                        stack.append(num)
                        m[num] -= 1
                    else:
                        break
                if m[num] == 0:
                    start += 1
            if len(stack) < 3:
                return False
            arr = arr[start:]
        return True


def main():
    s = Solution()
    print(s.isPossible([1,2,3,4,5,5,6]))
    print(s.isPossible([1,2,3,7,8,9]))
    print(s.isPossible([1,3,3,4,4,7,8,9]))


if __name__ == "__main__":
    main()
