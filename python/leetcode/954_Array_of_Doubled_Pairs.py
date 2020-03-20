# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        m = collections.Counter(A)
        A1 = sorted(list(filter(lambda x: True if x > 0 else False, A)))
        A2 = sorted(list(filter(lambda x: True if x < 0 else False, A)))
        for num in A1:
            if m.get(num, 0) != 0:
                if m.get(num*2, 0) != 0:
                    m[num*2] -= 1
                    m[num] -= 1
                else:
                    return False
        for num in A2[::-1]:
            if m.get(num, 0) != 0:
                if m.get(num*2, 0) != 0:
                    m[num*2] -= 1
                    m[num] -= 1
                else:
                    return False
        return True


def main():
    s = Solution()
    # print(s.canReorderDoubled([4,-2,2,-4]))
    # print(s.canReorderDoubled([3,1,3,6]))
    print(s.canReorderDoubled([-5,-3]))


if __name__ == "__main__":
    main()
