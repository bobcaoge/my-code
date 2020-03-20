# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        flag = 0

        while index2 < n and m > 0 and flag < m:

            # print(nums1, index1, index2)
            if nums1[index1] >= nums2[index2]:
                for index in range(len(nums1)-1, index1-1, -1):
                    nums1[index] = nums1[index-1]

                nums1[index1] = nums2[index2]
                index1 += 1
                index2 += 1
            else:
                index1 += 1
                flag += 1
            if index1 < len(nums1):
                if nums1[index1] < nums1[index1-1]:
                    break


        # print(nums1, index1, index2)
        # print("========================")
        while index2 < n:
            # print(nums1, index1, index2)
            nums1[index1] = nums2[index2]
            index1 += 1
            index2 += 1
        # print(nums1)

def main():
    s = Solution()
    s.merge([1,2,3,0,0,0],3,[2,5,6],3)
    s.merge([-1,0,0,3,3,3,0,0,0],3,[1,2,2],3)
    s.merge([0],0,[1],1)
    nums1 = [-1,-1,0,0,0,0]
    m = 4
    nums2 = [-1,0]
    n = 2
    s.merge(nums1, m, nums2, n)
    nums1 =[-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    m = 1
    nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
    n = 90
    s.merge(nums1, m, nums2, n)

if __name__ == "__main__":
    main()
