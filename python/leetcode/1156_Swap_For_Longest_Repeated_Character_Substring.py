# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        ret = 0
        for cur_letter in set(text):
            before = 0
            cur_length = 0
            not_used = 1
            for index, c in enumerate(text):
                if c != cur_letter:
                    if not_used > 0:
                        not_used -= 1
                    else:
                        cur_length = max(cur_length, index - before)
                        while text[before] == cur_letter:
                            before += 1
                        before += 1

            num = text.count(cur_letter)
            ret = max(ret, min(num, cur_length), min(num, len(text)-before))
        return ret


def main():
    s = Solution()
    print(s.maxRepOpt1("abab"))
    print(s.maxRepOpt1("aaabaaa"))
    print(s.maxRepOpt1("aaaaa"))
    print(s.maxRepOpt1("abcde"))
    print(s.maxRepOpt1("aaabbaaa"))


if __name__ == "__main__":
    main()
