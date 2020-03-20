# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def get_num(self, length):
        if length > 26:
            return (length - 25)*26 + 325
        else:
            return length*(length + 1) / 2

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0
        record = {}
        for i in range(26):
            record[chr(i+97)] = i

        m = [0]*26
        ret = 0
        for i in range(26):
            length = 0
            for index, c in enumerate(p):
                if length == 0:
                    if c == chr(i+97):
                        length = 1
                else:
                    if (record[p[index-1]] + 1) % 26 == record[c]:
                        length += 1
                    else:
                        m[i] = max(m[i], length)
                        length = 0 if c != chr(i+97) else 1
            m[i] = max(m[i], length)
            ret += m[i]
        return ret



def main():
    s = Solution()
    print(s.findSubstringInWraproundString("zabc"))
    print(s.findSubstringInWraproundString("rstuvwxyzabcdefghijklmnopqrstuvwxyzabc"))


if __name__ == "__main__":
    main()
