# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def get_roman_num(self, num, lower, higher, upper):
        """
        :type num: int
        :type lower: str
        :type higher: str
        :type upper: str
        :rtype: str
        """
        if num == 0:
            return ""
        elif 1 <= num <= 3:
            return lower*num
        elif num == 4:
            return lower+higher
        elif num <= 8:
            return higher+lower*(num-5)
        else:
            return lower+upper

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        letters = ["I", "V", "X", "L", "C", "D", "M", "", ""]
        index = 0
        ret = ""
        while num != 0:
            ret = self.get_roman_num(num % 10, letters[index], letters[index+1], letters[index+2]) + ret
            index += 2
            num = int(num / 10)
        return ret



def main():
    s = Solution()
    print(s.intToRoman(1994))
    print(s.intToRoman(58))


if __name__ == "__main__":
    main()
