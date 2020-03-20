# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        mid = int(n/2)
        while start != mid:
            if isBadVersion(mid):
                end = mid
                mid = int((end+start)/2)
            else:
                start = mid
                mid = int((end+start)/2)

        return end




def main():
    s = Solution()


if __name__ == "__main__":
    main()
