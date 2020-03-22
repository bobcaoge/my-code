# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        def get_step(num):
            ret = 0
            while num != 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = num*3+1
                ret += 1
            return ret
        nums = []
        for i in range(lo, hi+1):
            nums.append([get_step(i), i])
        return sorted(nums)[k-1][1]




def main():
    s = Solution()
    print(s.getKth(7,11,4))
    print(s.getKth(lo = 12, hi = 15, k = 2))


if __name__ == "__main__":
    main()
