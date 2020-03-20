# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ret = 0
        start = 0
        n = 0
        for index, c in enumerate(arr):

            a0 = start
            an = a0+n*1
            res = (a0+an)*(n+1)/2
            if res == sum(arr[start:index+1]):
                ret += 1
                start = index+1
                n = 0
            else:
                n += 1
        return ret


def main():
    s = Solution()
    print(s.maxChunksToSorted([1,0,2,3,4]))
    print(s.maxChunksToSorted([0,1,2,3,4]))
    print(s.maxChunksToSorted([4,3,2,1,0]))


if __name__ == "__main__":
    main()
