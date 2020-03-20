# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        pivot = 0
        maxL = A[0]
        max_last = 0
        for i, num in enumerate(A):
            max_last = max(max_last, num)
            if num < maxL:
                pivot = i
                maxL = max_last
        return pivot+1




    def partitionDisjoint2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        info = sorted([num, i] for i, num in enumerate(A))
        s = 0
        for index, (num, i) in enumerate(info):
            s += i
            if s == (index+1)*index/2:
                return index+1



def main():
    s = Solution()
    print(s.partitionDisjoint([5,0,3,8,6]))
    print(s.partitionDisjoint([1,1,1,0,6,12]))
    print(s.partitionDisjoint([1,1,8,10,1,6,12]))


if __name__ == "__main__":
    main()
