# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def step(num, pos):
            ret = []
            index = A.index(num)
            ret.append(index+1)
            A[:index+1] = A[:index+1][::-1]
            A[:pos+1] = A[:pos+1][::-1]
            ret.append(pos+1)
            return ret

        target = sorted(A)
        ret = []
        for i in range(len(A)-1, -1, -1):
            if A[i] != target[i]:
                ret.extend(step(target[i], i))
        return ret



def main():
    s = Solution()
    print(s.pancakeSort([3,2,4,1]))


if __name__ == "__main__":
    main()
