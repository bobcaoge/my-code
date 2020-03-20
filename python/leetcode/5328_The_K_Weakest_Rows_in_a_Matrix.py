# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        if not mat:
            return []
        rows = sorted([[sum(x), i] for i, x in enumerate(mat)])
        if k >= len(rows):
            return [i for _, i in rows]
        return [i for _, i in rows[:k]]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
