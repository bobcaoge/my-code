# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        info = {(0,0,0,0,0): -1}
        ret = 0
        cur = [0]*5
        index = {
                'a': 0,
                'e': 1,
                'i': 2,
                'o': 3,
                'u': 4
        }
        for pos, c in enumerate(s):
            if c in index:
                cur[index[c]] = (cur[index[c]]+1)%2
            if info.get(tuple(cur), pos) != pos:
                ret = max(ret, pos - info[tuple(cur)])
            else:
                info[tuple(cur)] = pos
        return ret

def main():
    s = Solution()
    print(s.findTheLongestSubstring("eleetminicoworoep"))


if __name__ == "__main__":
    main()
