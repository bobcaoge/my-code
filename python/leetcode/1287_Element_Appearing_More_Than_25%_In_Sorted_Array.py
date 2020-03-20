# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = 0
        cur = 0
        for num in arr:
            if num == cur:
                length += 1
            else:
                cur = num
                length = 1
            if length > len(arr) //4:
                return cur



def main():
    s = Solution()


if __name__ == "__main__":
    main()
