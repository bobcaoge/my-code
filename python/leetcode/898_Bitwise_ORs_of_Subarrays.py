# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        s.add(0)
        ans = set()
        for num in A:
            s = {num | y for y in s} | {num}
            ans |= s
        return len(ans)


def main():
    s = Solution()
    print(s.subarrayBitwiseORs([0]))
    print(s.subarrayBitwiseORs([1,1,2]))
    print(s.subarrayBitwiseORs([1,2,4]))


if __name__ == "__main__":
    main()
