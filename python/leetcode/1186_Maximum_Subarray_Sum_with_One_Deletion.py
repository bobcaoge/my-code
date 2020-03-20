# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp1 = [0]*len(arr)
        dp2 = [0]*len(arr)
        dp1[0] = arr[0]
        for i in range(1, len(arr)):
            dp1[i] = max(dp1[i-1]+arr[i], arr[i])

        dp2[-1] = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            dp2[i] = max(dp2[i+1]+arr[i], arr[i])
        ret = 0
        for i in range(len(arr)):
            ret = max(ret, max(0, (dp1[i-1] if i-1 >= 0 else 0))+max(0, (dp2[i+1] if i+1 < len(arr) else 0)))

        return ret if ret > 0 else max(arr)




def main():
    s = Solution()
    print(s.maximumSum([1,-4,-5,-2,5,0,-1,2]))
    print(s.maximumSum([-1,-1]))
    print(s.maximumSum([1,2,3,4]))
    print(s.maximumSum([1,-1,2,2,4]))
    print(s.maximumSum([1,1,1,100,1,-100,80]))
    print(s.maximumSum([1,1,100,-1,-1,90]))
    print(s.maximumSum([8,-1,6,-7,-4,5,-4,7,-6]))
    print(s.maximumSum([-1,5,5,-1,5,5,5]))
    print(s.maximumSum([11,-10,-11,8,7,-6,9,4,11,6,5,0]))


if __name__ == "__main__":
    main()
