# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B = sorted([(num, index) for index, num in enumerate(B)])
        remain = []
        j = 0
        ret = [0 for _ in range(len(A))]
        for i, num in enumerate(A):
            if num > B[j][0]:
                ret[B[j][1]] = num
                j += 1
            else:
                remain.append(num)
        for i in range(j, len(B)):
            ret[B[i][1]] = remain.pop()
        return ret


    def advantageCount2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        ret = [0]*len(A)
        for i in range(len(B)-1, -1, -1):
            index = bisect.bisect(A, B[i])
            if index < len(A) and A[index] > B[i]:
                ret[i] = A[index]
                A.pop(index)
            else:
                ret[i] = A[0]
                A.pop(0)
        return ret


def main():
    s = Solution()
    # print(s.advantageCount(A = [2,7,11,15], B = [1,10,4,11]))
    print(s.advantageCount(A = [12,24,8,32], B = [13,25,32,11]))


if __name__ == "__main__":
    main()
