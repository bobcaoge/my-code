# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 0:
            return str(hex(num))[2:]
        origin = [0] * 32
        origin[0] = 1
        place = 0
        num = -num
        while num != 0:
            origin[31-place] = num % 2
            place += 1
            num = int(num/2)
        print(origin)
        # 计算补码
        for i in range(1, 32):
            origin[i] = 0 if origin[i] == 1 else 1
        print(origin)
        carry = 1
        for i in range(1, 32):
            value = origin[32-i] + carry
            # print(i)
            origin[32-i] = value % 2
            carry = int(value/2)
            if carry == 0:
                break
        table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        ret = ""
        print(origin)
        for i in range(8):
            start = i*4
            end = start+4
            base = 1
            index = 0
            for j in origin[start:end]:
                index = index*2 + j
            ret += table[index]
        return ret






def main():
    s = Solution()
    print(s.toHex(-1))
    print(s.toHex(26))
    print(s.toHex(-2))

if __name__ == "__main__":
    main()
