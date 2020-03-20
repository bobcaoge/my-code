# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        ret = []
        info = []
        old = [0]*26
        for i, c in enumerate(s):
            cur = old.copy()
            cur[ord(c)-ord('a')] += 1
            info.append(cur)
            old = cur
        for left, right, k in queries:
            nums = 0
            for i in range(26):
                nums += (info[right][i]- (info[left-1][i] if left-1 >= 0 else 0)) % 2
            ret.append(k >= (nums//2))
        return ret







def main():
    s = Solution()


if __name__ == "__main__":
    main()
