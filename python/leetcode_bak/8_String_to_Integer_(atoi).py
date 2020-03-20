# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        pattern = re.compile(r"^[-+]{0,1}\d+")
        try:
            num_str_list = pattern.findall(str.split()[0])
        except:
            return 0
        # print(num_str_list)
        if num_str_list:
            num_str = num_str_list[0]
        else:
            return 0
        first = ""
        start = 0
        if num_str[0] == "-" or num_str[0] == "+":
            first = num_str[0]
            start = 1
        ret = 0
        int_max = 2147483647
        int_min = 2147483648
        for s in num_str[start:]:
            if first == "+" or first == "":
                if ret > int(int_max / 10) or ret == int(int_max / 10) and int(s) > 7:
                    return int_max
            if first == "-":
                if ret > int(int_min / 10) or ret == int(int_min / 10) and int(s) > 8:
                    return -int_min
            ret = ret*10 + int(s)
        if first == "-":
            ret = -ret
        # print(ret)
        return ret




def main():
    s = Solution()
    s.myAtoi("42")
    s.myAtoi("-42")
    s.myAtoi("4193 with words")
    s.myAtoi("words and 987")
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("-0 123"))
    print(s.myAtoi(""))


if __name__ == "__main__":
    main()
