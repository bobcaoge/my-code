# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flag = True
        cur = 1
        ret = 0
        A.append(1<<30)
        for i in range(1, len(A)):
            if flag:
                if A[i] > A[i-1]:
                    cur += 1
                elif A[i] == A[i-1]:
                    cur = 1
                else:
                    if cur > 1:
                        flag = not flag
                        cur += 1
                    else:
                        cur = 1
            else:
                if A[i] < A[i-1]:
                    cur += 1
                else:
                    flag = not flag
                    ret = max(ret, cur)
                    if A[i] == A[i-1]:
                        cur = 1
                    else:
                        cur = 2
        return ret


def main():
    s = Solution()
    print(s.longestMountain([2,1,4,7,3,2,5]))
    print(s.longestMountain([1,2,3,4,5,4,3,2,1,1,2,3,4,5,6,5,4,3,2,1]))
    print(s.longestMountain([1,2,1,2,3,2,1]))


if __name__ == "__main__":
    main()
