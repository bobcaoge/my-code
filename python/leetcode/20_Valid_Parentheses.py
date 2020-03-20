# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num_dic = {
            "(": -1,
            ")": 1,
            "[": -2,
            "]": 2,
            "{": -3,
            "}": 3,

        }
        s_list = []
        move = -1
        while move+1 < len(s):
            # print
            if not s_list:
                s_list.append(s[move])
            else:
                # print(s_list[-1], s[move+1])
                if num_dic[s_list[-1]] + num_dic[s[move+1]] == 0:
                    s_list.pop()
                    move += 1
                else:
                    s_list.append(s[move+1])
                    move += 1
            # print(s_list, move)
        if s_list:
            return False
        else:
            return True




def main():
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))


if __name__ == "__main__":
    main()
