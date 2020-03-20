# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort()
        length = len(citations)
        for i in range(length):
            if length - i <= citations[i] and citations[i] != 0:
                return length-i
        return 0



def main():
    s = Solution()


if __name__ == "__main__":
    main()
