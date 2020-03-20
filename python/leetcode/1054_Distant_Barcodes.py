# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        info = sorted([[times, num] for num, times  in collections.Counter(barcodes).items()], reverse=True)
        barcodes = []
        for times, num in info:
            barcodes.extend([num]*times)

        length = len(barcodes)
        if length == 1:
            return barcodes
        ret = [0]*length
        ret[0::2] = barcodes[:length//2+length%2][::-1]
        ret[1::2] = barcodes[length//2+length%2:][::-1]
        return ret


def main():
    s = Solution()
    print(s.rearrangeBarcodes([1,2]))
    print(s.rearrangeBarcodes([1,1,2]))
    print(s.rearrangeBarcodes([1,1,1,1,2,2,3,3]))
    print(s.rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8]))


if __name__ == "__main__":
    main()
