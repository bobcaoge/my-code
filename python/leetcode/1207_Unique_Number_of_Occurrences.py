# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        visited = set()
        for num, count in collections.Counter(arr).items():
            if count in visited:
                return False
            visited.add(count)
        return True



def main():
    s = Solution()


if __name__ == "__main__":
    main()
