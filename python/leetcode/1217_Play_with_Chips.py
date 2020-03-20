# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        # move to 0
        # move to 1
        a = 0
        b = 0
        for pos in chips:
            if pos % 2 == 0:
                b += 1
            else:
                a += 1
        return min(a, b)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
