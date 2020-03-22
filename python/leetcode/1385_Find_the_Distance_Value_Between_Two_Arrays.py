# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ret = 0
        for num in arr1:
            for num2 in arr2:
                if abs(num-num2) <= d:
                    break
            else:
                ret += 1
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
