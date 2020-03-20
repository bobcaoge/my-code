# /usr/bin/python3.6
# -*- coding:utf-8 -*-
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if not strs:
            return ""
        i = 0
        try:
            while True:
                prefix = strs[0][i]
                # print(prefix)
                for s in strs:
                    # print(s)
                    if s[i] != prefix:
                        return ret

                ret += prefix
                i += 1
        except:
            pass
        return ret



def main():
    s = Solution()
    strs = ["flower","flow","flight"]
    ret = s.longestCommonPrefix(strs)
    print(ret)


if __name__ == "__main__":
    main()
