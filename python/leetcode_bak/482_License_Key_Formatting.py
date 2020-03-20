# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re

class Solution(object):
    def licenseKeyFormatting1(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ret = ""
        cur = 0
        s = S.replace("-", "").upper()
        length = len(s)
        for i in range(length):
            index = length - i -1
            if cur == K:
                cur = 0
                ret = '-'+ret
            ret = s[index].upper() + ret
            cur += 1
        return ret

    def licenseKeyFormatting1(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace("-", "").upper()
        length = len(s)
        length_of_first_block = length % K
        i = length_of_first_block
        ret = s[:length_of_first_block]
        while i < length:
            ret += "-" + s[i: i+K]
            i += K

        return ret if length_of_first_block != 0 else ret[1:]

    def licenseKeyFormatting2(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace("-", "").upper()
        i = len(s)
        if i < K:
            return s
        ret = ""
        while i > 0:
            ret =s[i-K: i] + "-" + ret
            i -= K
        print(i)
        if i < 0:
            ret =s[: i+K] + ret
            ret = ret[0:-1]
        else:
            ret = ret[0:-1]

        return ret
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace("-", "").upper()
        length = len(s)
        i = length % K
        ret = s[:i]
        pattern = r"(\w{"+str(K)+"})"
        pattern = re.compile(pattern)
        last = pattern.findall(s[i:])
        if last:
            if ret:
                ret += "-" +"-".join(last)
            else:
                ret = "-".join(last)
        return ret

def main():
    s = Solution()
    print(s.licenseKeyFormatting(S = "5F3Z-2e-9-w", K = 4))
    print(s.licenseKeyFormatting(S = "2-5g-3-J", K = 2))
    print(s.licenseKeyFormatting(S = "2", K = 2))
    print(s.licenseKeyFormatting(S = "2-4A0r7-4k", K = 3))

if __name__ == "__main__":
    main()
