# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """


    def sortedSquares3(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index = 0
        length = len(A)
        while index < length:
            if A[index] >= 0:
                break
            index += 1
        first = index
        second = index-1
        ret = []
        while first < length or second >= 0:
            if first < length and second >= 0:
                a = A[first]*A[first]
                b = A[second]*A[second]
                if a < b:
                    ret.append(a)
                    first += 1
                else:
                    ret.append(b)
                    second -= 1
            elif first < length:
                ret.append(A[first]*A[first])
                first += 1
            elif second >= 0:
                ret.append(A[second]*A[second])
                second -= 1
        return ret

    def sortedSquares1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x * x for x in A])

    def sortedSquares2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        minus = []
        plus = []
        for i, num in enumerate(A):
            a = num*num
            if num >= 0:
                plus.append(a)
            else:
                minus.append(a)
        plus = plus[-1::-1]
        ret = []
        while minus or plus:
            if minus and plus:
                if minus[-1] < plus[-1]:
                    ret.append(minus.pop())
                else:
                    ret.append(plus.pop())
            elif minus:
                return ret+minus[-1::-1]
            elif plus:
                return ret+plus[-1::-1]
        return ret
def main():
    s = Solution()


if __name__ == "__main__":
    main()
