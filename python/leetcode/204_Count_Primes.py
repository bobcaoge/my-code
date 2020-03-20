# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution:

    def is_the_num(self, num):
        if num == 1:
            return False
        if num == 2:
            return True
        sq = int(math.sqrt(num))
        for i in range(2, sq+1):
            if num % i == 0:
                return False
        return True

    def countPrimes1(self, n: 'int') -> 'int':
        ret = 0 if n-1 < 2 else 1
        for i in range(1, n, 2):
            if self.is_the_num(i):
                # print(i)
                ret += 1

        return ret
    def countPrimes(self, n: 'int') -> 'int':
        # if n <= 1:
        #     return 0
        table = [True] * n
        table[0] = False
        table[1] = False
        for i in range(2, int(n**0.5)+1):
            table[i*i:n:i] = [False] * len(table[i*i:n:i])
        return sum(table)




def main():
    s = Solution()
    print(s.countPrimes(10))
    print(s.countPrimes(1))
    print(s.countPrimes(2))


if __name__ == "__main__":
    main()
