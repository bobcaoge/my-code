# /usr/bin/python3.6
# -*- coding:utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) == 0:
            length = len(nums1)
            if length%2 == 0:
                length = length -1
                return (nums1[int(length/2)] + nums1[int(length/2)+1])/2
            else:
                if length == 1:
                    return nums1[0]
                else:
                    return nums1[int(length/2)+1]

        if len(nums1) == 0:
            length = len(nums2)
            if length%2 == 0:
                    length -= 1
                    return (nums2[int(length/2)] + nums2[int(length/2)+1])/2
            else:
                if length == 1:
                    return nums1[0]
                else:
                    return nums2[int(length/2)+1]

        length1 = len(nums1)
        length2 = len(nums2)
        length = length1+length2
        start_l1 = 0
        end_l1 = length1 - 1
        mid_1 = int((end_l1+start_l1)/2)
        start_l2= 0
        end_l2 = length2 - 1
        mid_2 = int((end_l2+start_l2)/2)
        # 先在2中找1，再在1中找2，然后进行判断
        # 设置有效位置
        efficient_start_l1 = 0
        efficient_end_l1 = length1 - 1
        efficient_start_l2 = 0
        efficient_end_l2 = length2 - 1
        while start_l1 != mid_1 and start_l2 != mid_2:

            print("L1", start_l1, mid_1, end_l1)
            print("L2", start_l2, mid_2, end_l2)
            # 固定1，找2
            while start_l1 < end_l1 and start_l2 < end_l2:
                # 判断中间位置
                if nums1[mid_1] >= nums2[mid_2]:
                    # 中间位置的后一位存在
                    if mid_2 + 1 <= efficient_end_l2:
                        # 判断中间位置的后一位
                        if nums1[mid_1] <= nums2[mid_2+1]:
                            break
                        else:
                            # 未找到 改变区域继续查找
                            start_l2 = mid_2 + 1
                            mid_2 = int((end_l2+start_l2)/2)
                            # efficient_start_l2 = start_l2
                            # efficient_end_l2 = end_l2
                    else:
                        break
                if nums1[mid_1] < nums2[mid_2]:
                    # 中间位置的前一位存在
                    if mid_2 - 1 >= efficient_start_l2:
                        # 判断中间位置的后一位
                        if nums1[mid_1] >= nums2[mid_2-1]:
                            break
                        else:
                            # 未找到 改变区域继续查找
                            end_l2 = mid_2 - 1
                            mid_2 = int((end_l2+start_l2)/2)
                            # efficient_start_l2 = start_l2
                            # efficient_end_l2 = end_l2
                    else:
                        break
                # print("L1", start_l1, mid_1, end_l1)
                # print("L2", start_l2, mid_2, end_l2)
            # print(nums1[mid_1], nums2[mid_2])

            # if start_l1 == mid_1 and start_l2 == mid_2:
            #     break
            print("L1   ", start_l1, mid_1, end_l1)
            print("L2   ", start_l2, mid_2, end_l2)
            if mid_2 < (efficient_start_l2+efficient_end_l2)/2:
                end_l2 = efficient_end_l2 - (mid_1 - efficient_start_l1)
                start_l2 = mid_2
                end_l1 = efficient_end_l1-(mid_2 - efficient_start_l2)
                start_l1 = mid_1
            else:
                # 可能不对
                start_l1 = efficient_start_l1 + efficient_end_l2 - end_l2
                end_l1 = mid_1
                start_l2 = efficient_start_l2 + efficient_end_l1 - end_l1
                end_l2 = mid_2

            mid_1 = int((end_l1+start_l1)/2)
            mid_2 = int((end_l2+start_l2)/2)
            efficient_end_l2 = end_l2
            efficient_end_l1 = end_l1
            efficient_start_l2 = start_l2
            efficient_start_l1 = start_l1
            # 判断结束条件

        print("L1", start_l1, mid_1, end_l1)
        print("L2", start_l2, mid_2, end_l2)
        print(nums1[mid_1], nums2[mid_2])
        # 奇偶处理
        # 偶数
        if length % 2 == 0:
            if length - mid_2 - mid_1 > length/2:
                return (nums1[mid_1+1] + nums2[mid_2])/2
        else:
            return nums2[mid_2]


def main():
    s = Solution()
    # nums1 = [3]
    # nums2 = [-2,-1]
    nums2 = [2,4,6,8]
    nums1 = [1,3,5,7,9]
    ret = s.findMedianSortedArrays(nums1,nums2)
    print(ret)


if __name__ == "__main__":
    main()
