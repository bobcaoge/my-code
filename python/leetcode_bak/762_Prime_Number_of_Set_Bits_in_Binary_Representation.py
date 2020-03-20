# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        def is_prime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        ret = 0
        for i in range(L, R + 1):
            if is_prime(bin(i).count("1")):
                ret += 1
        return ret

    def countPrimeSetBits1(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes for x in range(L, R+1))

def main():
    s = Solution()


if __name__ == "__main__":
    main()
