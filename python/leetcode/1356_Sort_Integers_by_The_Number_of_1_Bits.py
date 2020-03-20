# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        info = [[bin(x).count('1'), x] for x in arr]
        info.sort()
        return [x for _, x in info]



def main():
    s = Solution()
    print(s.sortByBits([0,1,2,3,4,5,6,7,8]))
    print(s.sortByBits([3, 8]))


if __name__ == "__main__":
    main()
