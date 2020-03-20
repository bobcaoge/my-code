# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        ret = [-1]
        last = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            ret.append(last)
            last = max(last, arr[i])
        return ret[::-1]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
