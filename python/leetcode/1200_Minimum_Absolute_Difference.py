# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        arr.sort()
        diffs = [arr[i+1]-arr[i] for i in range(len(arr)-1)]
        min_diff = min(diffs)
        for i, diff in enumerate(diffs):
            if diff == min_diff:
                ret.append([arr[i], arr[i+1]])
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
