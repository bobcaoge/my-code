# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        ret = 0
        cur_max = -1
        for i, num in enumerate(A):
            if num > cur_max:
                cur_max = num
            else:
                ret += cur_max+1-num
                cur_max += 1
        return ret


def main():
    s = Solution()
    print(s.minIncrementForUnique([1,2,2]))
    print(s.minIncrementForUnique([3,2,1,2,1,7]))


if __name__ == "__main__":
    main()
