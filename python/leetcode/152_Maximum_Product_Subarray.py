# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def get_max_product(self, info):
        """
        :type info: list[list[], int]
        :rtype: int
        """
        if len(info[0]) == 1:
            return info[0][0]
        ret = 1
        if info[1] % 2 == 0:
            for num in info[0]:
                ret *= num
        else:
            flag = False
            for index, num in enumerate(info[0]):
                if flag:
                    ret *= num
                if not flag and num < 0:
                    flag = True
            first = ret

            flag = False
            ret = 1
            for index, num in enumerate(info[0][-1::-1]):
                if flag:
                    ret *= num
                if not flag and num < 0:
                    flag = True
            ret = max(first, ret)

        return ret
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        info = []
        minus_number = 0
        nums.append(0)
        zero_flag = False
        for i, num in enumerate(nums):
            if num == 0:
                if i != len(nums)-1:
                    zero_flag = True
                if i > start:
                    info.append([nums[start:i], minus_number])
                minus_number = 0
                start = i+1
            elif num < 0:
                minus_number += 1
        # print(info)
        ret = -2**32
        for item in info:
            ret = max(self.get_max_product(item), ret)
            # print(ret)
        return max(ret,0) if zero_flag else ret


def main():
    s = Solution()
    # print(s.maxProduct([2,3,-2,4]))
    # print(s.maxProduct([-2,0,-1]))
    # print(s.maxProduct([0,1,2,3,4,5,0,1,2,32,0,-1,0,-2]))
    print(s.maxProduct([-2]))


if __name__ == "__main__":
    main()
