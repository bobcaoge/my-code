# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        index1 = 0
        index2 = length - 1
        sum = 0
        while index1 < index2:
            sum = numbers[index1] + numbers[index2]
            if sum == target:
                return [index1+1, index2+1]
            elif sum > target:
                index2 -= 1
            else:
                index1 += 1



def main():
    s = Solution()


if __name__ == "__main__":
    main()
