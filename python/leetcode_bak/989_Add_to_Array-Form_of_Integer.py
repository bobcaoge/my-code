# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if not K or K == 0:
            return A

        k_list = []
        index = len(A) - 1
        jinwei = 0
        while K != 0 or jinwei != 0:
            buffer = K%10
            if index >= 0:
                result = A[index] + buffer + jinwei
                A[index] = result % 10
                jinwei = int(result /10)
                # print(jinwei)
            else:
                # print(True)
                result = buffer + jinwei
                A.insert(0, result % 10)
                jinwei = int(result /10)
            # print(index)
            index -= 1

            K = int(K/10)

        return A


def main():
    s = Solution()
    print( s.addToArrayForm([1,2,3,4], 0))
    print( s.addToArrayForm([1], 1234))
    print( s.addToArrayForm([1,2,3,4], 1234))
    print( s.addToArrayForm([], 1234))
    print( s.addToArrayForm([2,1,5], 806))
    print( s.addToArrayForm([9,9,9,9,9], 1))



if __name__ == "__main__":
    main()
