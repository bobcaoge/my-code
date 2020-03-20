# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(s, flag):
            """
            :type s: str
            :type flag: bool
            :return:
            """
            pos1 = s.find("(")
            if pos1 == -1:
                return s if not flag else s[::-1]
            else:
                count = 1
                pos2 = -1
                for i in range(pos1+1, len(s)):
                    if s[i] == "(":
                        count += 1
                    elif s[i] == ")":
                        count -= 1
                        if count == 0:
                            pos2 = i
                            break
                center = reverse(s[pos1+1:pos2], not flag)
                right = reverse(s[pos2+1:], flag)

                if flag:
                    return right+center+s[:pos1][::-1]
                return s[:pos1] + center + right
        return reverse(s, False)



def main():
    s = Solution()
    print(s.reverseParentheses("(i(love)u)"))
    print(s.reverseParentheses("abc(123)abc"))
    print(s.reverseParentheses("ta()usw((((a))))"))


if __name__ == "__main__":
    main()
