# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        diff = []
        m = [0] * 26
        flag = False
        for i in range(len(A)):
            if not flag:
                m[ord(A[i])-97] += 1
                if m[ord(A[i])-97] == 2:
                    flag = True
            if A[i] != B[i]:
                diff.append(i)
                if len(diff) == 3:
                    return False
        if len(diff) == 0:
            if flag:
                return True
            else:
                return False
        if len(diff) == 1:
            return False
        diff_a = A[diff[1]]+A[diff[0]]
        diff_b = B[diff[0]]+B[diff[1]]
        return diff_a == diff_b


def main():
    s = Solution()


if __name__ == "__main__":
    main()
