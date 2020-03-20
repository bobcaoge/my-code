# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index_of_odd = 1
        index_of_even = 0
        ret = [0]*len(A)
        for num in A:
            if num % 2 == 1:
                ret[index_of_odd] = num
                index_of_odd += 2
            else:
                ret[index_of_even] = num
                index_of_even += 2
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
