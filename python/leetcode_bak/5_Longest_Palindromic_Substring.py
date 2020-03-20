# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s
        move = 0
        judge = 0
        max_num = 1
        cur_num = 0
        cur = ""
        real_ret = s[move]
        first_flag = True
        old_center = 0
        while move < len(s):
            # print(cur, cur_num, real_ret, max_num, move, judge)
            # 重新开始
            if first_flag:
                cur_num = 0
                # 课向后拓展
                if move+1 < len(s):
                    # 无相邻相同
                    if s[move] != s[move+1]:
                        # 可向前延伸
                        if judge - 1 >=0:
                            # 类似aba的间隔一个相同
                            if s[judge-1] == s[move+1]:
                                cur = s[judge-1] + s[move] + s[move+1]
                                cur_num += 3
                                judge -= 1
                                move += 1
                                first_flag = False
                            # 既无相邻相同，也无间隔一个相同
                            else:
                                # move = int((move + judge)/2)+1
                                move += 1
                                judge = move
                        # 不可向前延伸
                        else:
                            # move = int((move + judge)/2)+1
                            move += 1
                            judge = move
                    # 有相邻相同
                    else:
                        cur = s[move] + s[move+1]
                        # print(cur)
                        cur_num += 2
                        first_flag = False
                        move += 1
                        # 可向前扩展
                        if judge-1 >= 0:
                            # 连续相同判断
                            while judge-1 >= 0 and s[judge-1] == s[move]:
                                cur += s[move]
                                cur_num += 1
                                judge -= 1
                            else:
                                if cur_num >= max_num:
                                    real_ret = cur
                                    max_num = cur_num
                        # 不可向前扩展
                        else:
                            first_flag = True
                            if cur_num >= max_num:
                                real_ret = cur
                                max_num = cur_num
                                cur = ""
                            judge = move
                # 不可向后拓展
                else:
                    break
            # 非重新开始
            else:
                # 可向后扩展
                if move+1 < len(s):
                    if judge - 1 >= 0:

                        if s[judge-1] == s[move+1]:
                            cur = s[judge-1] + cur + s[move+1]
                            # print(cur)
                            cur_num += 2
                            judge -= 1
                            move += 1
                            first_flag = False
                        else:
                            first_flag = True
                            if int((move + judge)/2)+1 <= old_center:
                                move = old_center +1
                            else:
                                move = int((move + judge)/2)+1

                            old_center = move
                            judge = move
                            if cur_num >= max_num:
                                real_ret = cur
                                max_num = cur_num
                                cur = ""
                    else:
                        if cur_num >= max_num:
                            real_ret = cur
                            max_num = cur_num
                            cur = ""
                        if int((move + judge)/2)+1 <= old_center:
                            move = old_center +1
                        else:
                            move = int((move + judge)/2)+1
                        old_center = move
                        judge = move
                        first_flag = True
                # 不可向后拓展
                else:
                    break
        if cur_num>max_num:
            real_ret = cur
        return real_ret

def main():
    s = Solution()
    # print(s.longestPalindrome("babad"))
    # print(s.longestPalindrome("cbbd"))
    # print(s.longestPalindrome("abcdefg"))
    # print(s.longestPalindrome(""))
    # print(s.longestPalindrome("a"))
    # print(s.longestPalindrome("ccc"))
    # print(s.longestPalindrome("aba"))
    # print(s.longestPalindrome("abadd"))
    # print(s.longestPalindrome("babadada"))
    # print(s.longestPalindrome("abababababa"))
    # print(s.longestPalindrome("ababababababa"))
    # print(s.longestPalindrome("aaabaaaa"))
    # print(s.longestPalindrome("tattarrattat"))
    # print(s.longestPalindrome("aaaabaaa"))
    print(s.longestPalindrome("dddddddd"))


if __name__ == "__main__":
    main()
