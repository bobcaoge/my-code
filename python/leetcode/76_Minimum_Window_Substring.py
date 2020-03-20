# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def judge(a, b):
            for i in range(len(a)):
                if a[i] < b[i]:
                    return False
            return True

        target = [0]*128
        cur = [0]*128
        i = 0
        ret = ""
        for c in t:
            target[ord(c)] += 1
        for j, c in enumerate(s):
            cur[ord(c)] += 1
            if judge(cur, target):
                while cur[ord(s[i])] > target[ord(s[i])]:
                    cur[ord(s[i])] -= 1
                    i += 1
                if len(ret) > j-i+1 or ret == "":
                    ret = s[i:j+1]
        return ret


def main():
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))


if __name__ == "__main__":
    main()
