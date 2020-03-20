# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        heap = []
        for i, x in enumerate(A):
            if A[i] < 0:
                if K > 0:
                    heapq.heappush(heap, (-A[i], i))
                    K -= 1
                    A[i] = -A[i]
                else:
                    num, index = heapq.heappop(heap)
                    if num < -A[i]:
                        A[index] = -num
                        heapq.heappush(heap, (-A[i], i))
                        A[i] = -A[i]
        ret = sum(A)
        if K % 2 == 1:
            return ret - 2*min(sum)
        return ret


    def largestSumAfterKNegations_1(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        num_of_negation = len([x for x in A if x < 0])
        if K == num_of_negation:
            return sum([abs(x) for x in A])
        elif K > num_of_negation:
            if (K-num_of_negation)%2 == 0:
                return sum([abs(x) for x in A])
            else:
                return sum([abs(x) for x in A]) - 2*min([abs(x) for x in A])
        else:
            heapq.heapify(A)
            while K > 0:
                num  = heapq.heappop(A)
                heapq.heappush(A, -num)
                K -= 1
            return sum(A)





def main():
    s = Solution()


if __name__ == "__main__":
    main()
