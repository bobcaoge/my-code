# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        indexes = [0]*len(primes)
        ugly_numbers = [2**32]*n
        ugly_numbers[0] = 1
        i = 1
        while i < n:
            # print(ugly_numbers)
            # print(indexes)
            index = -1
            next_ = ugly_numbers[i]
            for index_of_j, prime in enumerate(primes):
                next_ugly_number = ugly_numbers[indexes[index_of_j]]*prime
                if next_ugly_number < next_:
                    next_ = next_ugly_number
                    index = index_of_j
            indexes[index] += 1
            if next_ > ugly_numbers[i-1]:
                ugly_numbers[i] = next_
                i += 1
        # print(ugly_numbers)
        return ugly_numbers[-1]


def main():
    s = Solution()
    print(s.nthSuperUglyNumber(1900, [2, 7, 13, 19]))


if __name__ == "__main__":
    main()
