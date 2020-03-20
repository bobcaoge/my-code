# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        m = {}
        for c in s:
            m[c] = m.get(c, 0)+1
        less_than_k = set()
        flag = True
        for key, value in m.items():
            if value < k:
                less_than_k.add(key)
                flag = False
        if flag:
            return len(s)

        last = 0
        ret = 0
        i = 0
        while i < len(s):
            if s[i] in less_than_k:
                if i > last:
                    ret = max(ret, self.longestSubstring(s[last:i], k))
                last = i+1
            i += 1

        if last < len(s):
            ret = max(ret, self.longestSubstring(s[last:], k))
        return ret


def main():
    s = Solution()
    print(s.longestSubstring("aaabb", 3))
    print(s.longestSubstring("ababbc", 2))


if __name__ == "__main__":
    main()
