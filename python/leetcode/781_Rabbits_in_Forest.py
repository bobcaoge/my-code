# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        m = collections.Counter(answers)
        ret = 0
        for num_in_back, num_of_the_same_color in m.items():
            d, l = divmod(num_of_the_same_color, num_in_back+1)
            ret += (num_in_back+1) * (d + (1 if l > 0 else 0))
        return ret


def main():
    s = Solution()
    print(s.numRabbits([1, 1, 2]))
    print(s.numRabbits([10, 10, 10]))


if __name__ == "__main__":
    main()
