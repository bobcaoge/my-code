# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        start = 0
        end = length-1
        mid = (start+end)/2
        last = -1
        while start <= end:
            if length-mid <= citations[mid] != 0:
                last = length-mid
                end = mid-1
            else:
                start = mid+1
            mid = (start+end)/2
        return last if last != -1 else 0


def main():
    s = Solution()


if __name__ == "__main__":
    main()
