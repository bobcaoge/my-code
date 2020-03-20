# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        m = {0:1}
        cur_sum = 0
        ret = 0
        for num in A:
            cur_sum += num
            ret += m.get(cur_sum-S, 0)
            m[cur_sum] = m.get(cur_sum, 0) + 1
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
