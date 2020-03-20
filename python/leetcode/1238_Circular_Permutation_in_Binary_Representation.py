# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        step = [0]
        for i in range(n):
            next_step = [num<<1 for num in step] + [(num<<1)+1 for num in step][::-1]
            step = next_step
        index_of_start = step.index(start)
        return step[index_of_start:]+step[:index_of_start]


def main():
    s = Solution()
    print(s.circularPermutation(2, 2))
    print(s.circularPermutation(1, 0))
    print(s.circularPermutation(5, 0))


if __name__ == "__main__":
    main()
