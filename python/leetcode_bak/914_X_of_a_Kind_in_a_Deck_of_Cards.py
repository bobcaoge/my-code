# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def get_factors(self, num):
        ret = []
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                ret.append(i)
                ret.append(num / i)
        return ret + [num]

    def remove_factor(self, num, factors):
        i = 0
        while i < len(factors):
            if num % factors[i] != 0:
                factors.remove(factors[i])
            else:
                i += 1

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        m = {}
        for card in deck:
            m[card] = m.get(card, 0) + 1
        min_times = min([value for key, value in m.items()])
        if min_times < 2:
            return False
        factors = self.get_factors(min_times)
        # print(factors)
        # print(m)
        for times in m.values():
            self.remove_factor(times, factors)
            if not factors:
                return False
        return True


def main():
    s = Solution()


if __name__ == "__main__":
    main()
