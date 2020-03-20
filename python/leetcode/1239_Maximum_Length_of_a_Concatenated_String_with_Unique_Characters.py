# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        arr = filter(lambda x:len(set(x)) == len(x), arr)
        cur = [[set(), 0]]
        for s in arr:
            buff = []
            buff.append([set(s), len(s)])
            letters = set(s)
            for old_set, length in cur:
                if not (letters & old_set):
                    buff.append([old_set | letters, length+len(s)])
            cur.extend(buff)
        return max([length for _, length in cur])


def main():
    s = Solution()
    print(s.maxLength(["cha","r","act","ers"]))


if __name__ == "__main__":
    main()
