# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    def convertToBase7(self, num: 'int') -> 'str':
        if num == 0:
            return "0"
        ret = ""
        minus_flag = True if num < 0 else False
        num = abs(num)
        while num != 0:
            ret = str(num%7) + ret
            num = int(num/7)
        return ret if not minus_flag else "-"+ret



def main():
    s = Solution()
    print(s.convertToBase7(0))
    print(s.convertToBase7(100))
    print(s.convertToBase7(-100))
    print(s.convertToBase7(-7))


if __name__ == "__main__":
    main()
