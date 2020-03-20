# /usr/bin/python3.6
# -*- coding:utf-8 -*-
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_list = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return num_list[s]
        ret = 0
        move = 0
        while move + 1 < len(s) :
            if num_list[s[move]] < num_list[s[move+1]]:
                buffer = num_list[s[move+1]]-num_list[s[move]]
                move += 2
            else:
                buffer = num_list[s[move]]
                move += 1
            ret += buffer

        if move < len(s):
            ret += num_list[s[move]]
        # print(ret)
        return ret



def main():
    s = Solution()
    s.romanToInt("III")
    s.romanToInt("IV")
    s.romanToInt("IX")
    s.romanToInt("LVIII")
    s.romanToInt("MCMXCIV")



if __name__ == "__main__":
    main()
