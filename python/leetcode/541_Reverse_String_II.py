# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        end = 2*k
        ret = ""
        while end < len(s):
            ret += s[end-2*k:end-k][-1::-1]
            ret += s[end-k:end]
            end += 2*k
        length_ret = len(ret)
        if len(s) - length_ret < k:
            ret += s[end-2*k:end-k][-1::-1]
        else:
            ret += s[end-2*k:end-k][-1::-1]
            ret += s[end-k:end]
        return ret

def main():
    s = Solution()
    print(s.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",39))


if __name__ == "__main__":
    main()
