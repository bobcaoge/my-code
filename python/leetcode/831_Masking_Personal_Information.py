# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if "@" in S:
            return self.mask_email(S)
        return self.mask_phone_number(S)

    def mask_email(self, email):
        email = email.lower()
        names = email.split("@")
        return names[0][0]+"*****"+names[0][-1]+"@"+names[1]


    def mask_phone_number(self, phone_number):
        number = re.sub(r"-|\(|\)|\+| ", "", phone_number)
        if len(number) == 10:
            return "***-***-"+number[-4:]
        else:
            return "+"+"*"*(len(number)-10)+"-***-***-"+number[-4:]


def main():
    s = Solution()
    print(s.maskPII("LeetCode@Leetcode.com"))
    print(s.maskPII("12345678900"))


if __name__ == "__main__":
    main()
