# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_values = 0
        ret = []
        for value in A:
            if value %2 == 0:
                even_values += value

        for value, index  in queries:

            if A[index] %2 ==0:
                even_values -= A[index]
            A[index] += value
            if A[index] %2 ==0:
                even_values += A[index]
            ret.append(even_values)
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
