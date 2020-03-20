# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        pos1 = len(arr1)-1
        pos2 = len(arr2)-1
        ret = []
        carry = 0
        while pos1 >= 0 or pos2 >= 0:
            num1 = arr1[pos1] if pos1 >= 0 else 0
            num2 = arr2[pos2] if pos2 >= 0 else 0
            num = num1 + num2 +carry
            if num >= 2:
                ret.append(num-2)
                carry = -1
            elif num == -1:
                ret.append(1)
                carry = 1
            else:
                ret.append(num)
                carry = 0
            pos1 -= 1
            pos2 -= 1
        if carry == -1:
            ret.extend([1,1])
        elif carry == 1:
            ret.append(1)
        while ret and ret[-1] == 0:
            ret.pop()
        return ret[::-1] if ret else [0]




def main():
    s = Solution()
    print(s.addNegabinary([1,1,1,1,1], [1,0,1]))
    print(s.addNegabinary([0], [1, 0]))
    print(s.addNegabinary([1,0], [1, 0]))
    print(s.addNegabinary([1,1], [1]))


if __name__ == "__main__":
    main()
