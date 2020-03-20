# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        rotate_map = {
            0: 0,
            1: 1,
            2: 5,
            5: 2,
            6: 9,
            8: 8,
            9: 6,
        }

        def is_good_number(num):
            check = num
            rotate_num = 0
            base = 0
            while num:
                buffer = rotate_map[num % 10]
                rotate_num += buffer*(10**base)
                base += 1
                num = int(num/10)
            return rotate_num != check
        ret = 0
        pattern = re.compile(r"3?4?7?")
        for i in range(1, N+1):
            if not "".join(pattern.findall(str(i))) and is_good_number(i):
                # print(i)
                ret += 1
        return ret
    def rotatedDigits1(self, N):
        """
        :type N: int
        :rtype: int
        """
        rotate_map = {
            0: 0,
            1: 1,
            2: 5,
            3: -1,
            4: -1,
            5: 2,
            6: 9,
            7: -1,
            8: 8,
            9: 6,
        }

        def is_good_number(num):
            check = num
            rotate_num = 0
            base = 0
            while num:
                buffer = rotate_map[num % 10]
                if buffer != -1:
                    rotate_num += buffer*(10**base)
                else:
                    return False
                base += 1
                num = int(num/10)
            return rotate_num != check
        ret = 0
        for i in range(1, N+1):
            if is_good_number(i):
                # print(i)
                ret += 1
        return ret

def main():
    s = Solution()
    print(s.rotatedDigits(10))


if __name__ == "__main__":
    main()
