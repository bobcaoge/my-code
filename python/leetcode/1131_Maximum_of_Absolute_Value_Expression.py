# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        ret = 0
        last1 = arr1[0]+arr2[0]
        last2 = arr2[0]-arr1[0]
        last3 = arr1[0]+arr2[0]
        last4 = arr2[0]-arr1[0]

        for i in range(len(arr1)):
            ret = max(ret, arr1[i]+arr2[i]+i - last1)
            last1 = min(last1, arr1[i]+arr2[i]+i)

            ret = max(ret, arr2[i]-arr1[i]+i - last2)
            last2 = min(last2, arr2[i]-arr1[i]+i)

            ret = max(ret, i-arr1[i]-arr2[i] + last3)
            last3 = max(last3, arr1[i] + arr2[i]-i)

            ret = max(ret, arr1[i]-arr2[i]+i + last4)
            last4 = max(last4, arr2[i]-arr1[i]-i)
        return ret


def main():
    s = Solution()
    print(s.maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))


if __name__ == "__main__":
    main()
