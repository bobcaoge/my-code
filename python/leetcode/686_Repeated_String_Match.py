# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def repeatedStringMatch1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        length_a = len(A)
        length_b = len(B)
        if length_a >= length_b:
            repeat = 1
        else:
            repeat = int(length_b/length_a)
        max_repeat = len(B)/len(A) + 3
        s = A*repeat
        while repeat < max_repeat:
            if s.find(B) >= 0:
                return repeat
            s += A
            repeat += 1
        return -1

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not B or A.find(B) >= 0:
            return 1
        length_a = len(A)
        start = -1
        for i in range(len(B) - length_a):
            if B[i:i+length_a] == A:
                start = i
                break
        if start == -1:
            if (A*2).find(B) >= 0:
                return 2






def main():
    s = Solution()
    print(s.repeatedStringMatch("aa", "a"))
    print(s.repeatedStringMatch("abcd", "bcdabcda"))
    print(s.repeatedStringMatch("abcd", "abcdabcd"))
    print(s.repeatedStringMatch("abcd", "abcdabcda"))
    print(s.repeatedStringMatch("abc", "cabcabca"))


if __name__ == "__main__":
    main()
