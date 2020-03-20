# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        def get_label_from_absolute_num(num):
            if num == 1:
                return 1
            k = int(math.log2(num))+1
            nums_before_k_row = (2<<(k-2)) - 1
            if k % 2 == 0:
                return (2 << k-1) - (num - nums_before_k_row)
            else:
                return num
        absolute_num = get_label_from_absolute_num(label)
        ret = []
        ret.append(label)
        while ret[-1] != 1:
            absolute_num //= 2
            ret.append(get_label_from_absolute_num(absolute_num))
        return ret[::-1]





def main():
    s = Solution()
    print(s.pathInZigZagTree(3))
    print(s.pathInZigZagTree(14))
    print(s.pathInZigZagTree(26))


if __name__ == "__main__":
    main()
