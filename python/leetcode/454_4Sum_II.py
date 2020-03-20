# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        m1 = {}
        for num_1 in A:
            for num_2 in B:
                buffer = num_1+num_2
                count = m1.get(buffer, 0)
                m1[buffer] = count+1

        ret = 0
        for num_1 in C:
            for num_2 in D:
                ret += m1.get(-num_1-num_2, 0)
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
