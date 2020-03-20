# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(s1, s2):
            p1 = 0
            p2 = 0
            while p1 < len(s1) and p2 < len(s2):
                if s1[p1] > s2[p2]:
                    return -1
                elif s1[p1] < s2[p2]:
                    return 1
                else:
                    p1 += 1
                    p2 += 1
            if p1 < len(s1):
                return 1
            if p2 < len(s2):
                return -1
            return 0
        s = sorted([str(x) for x in nums], compare)
        return "".join(s)





def main():
    s = Solution()
    print(s.largestNumber([1,22,11,9,5,2]))


if __name__ == "__main__":
    main()
