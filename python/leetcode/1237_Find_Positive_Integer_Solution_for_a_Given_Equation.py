# /usr/bin/python3.6
# -*- coding:utf-8 -*-


"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type z: int
        :rtype: List[List[int]]
        """
        def binary_search(x):
            start = 1
            end = 1000
            mid = (start + end)//2
            while start <= end:
                cur_val = customfunction.f(x, mid)
                if cur_val == z:
                    return mid
                elif cur_val > z:
                    end = mid - 1
                else:
                    start = mid + 1
                mid = (start + end)//2
            return -1
        ret = []
        for x in range(1, 1001):
            y = binary_search(x)
            if y != -1:
                ret.append([x, y])
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
