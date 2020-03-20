# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        base = 9
        num_of_layer = 1
        add = 9
        while n > add:
            base *= 10
            num_of_layer += 1
            add += base*num_of_layer
        # 回复到上一层
        add -= base*num_of_layer
        print("add:", add)
        start = base/9-1
        print("base:", base)
        print("num_of_layer", num_of_layer)
        # 计算距离base的偏移量
        offset = int((n-add)/num_of_layer)
        print("offset:", offset)
        num = int(start + offset)
        print(num, "==")
        # 计算位偏移量
        bit_offset = n - add - offset*num_of_layer
        print(bit_offset)
        if bit_offset == 0:
            return int(str(num)[-1])
        else:
            return int(str(num+1)[bit_offset-1])




def main():
    s = Solution()
    # print(s.findNthDigit(3))
    print(s.findNthDigit(11))
    print(s.findNthDigit(19))
    print(s.findNthDigit(1000))
    print(s.findNthDigit(99))
    print(s.findNthDigit(999999999))

if __name__ == "__main__":
    main()
