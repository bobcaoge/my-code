# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m = {0:1}
        sum_of_old_nums = 0
        ret = 0
        for num in A:
            sum_of_old_nums = (sum_of_old_nums+num) % K
            ret += m.get(sum_of_old_nums, 0)
            m[sum_of_old_nums] = m.get(sum_of_old_nums, 0) + 1
        return ret




def main():
    s = Solution()
    print(s.subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5))


if __name__ == "__main__":
    main()
