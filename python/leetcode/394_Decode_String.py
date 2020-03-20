# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        last = ""
        i = 0
        ret = ""
        while i<len(s):
            c = s[i]
            if "0" <= c <= "9":
                last += c
            else:
                if last == "":
                    ret += c
                else:
                    number = int(last)
                    if c == "[":
                        start = i
                        square_bracket = 1
                        anti_square_bracket = 0
                        i += 1
                        while square_bracket > anti_square_bracket:
                            if s[i] == "[":
                                square_bracket += 1
                            elif s[i] == "]":
                                anti_square_bracket += 1
                            i += 1
                        i -= 1
                        ret += number * self.decodeString(s[start+1:i])
                    last = ""
            i += 1
        return ret



def main():
    s = Solution()
    print(s.decodeString("abcd3[a]"))
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("2[abc]3[cd]ef"))

if __name__ == "__main__":
    main()
