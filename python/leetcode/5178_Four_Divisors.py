# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def valid(num):
            divisors = set()
            for i in range(1, int(math.sqrt(num))+1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num//i)
                if len(divisors) > 4:
                    return False
            return sum(divisors) if len(divisors) == 4 else 0
        ret = 0
        for num in nums:
            ret += valid(num)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
