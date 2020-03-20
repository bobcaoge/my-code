# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return
        ret = []
        window_length = len(p)
        target = list(p)
        target.sort()
        for i in range(len(s)-len(p)+1):
            buffer = list(s[i:window_length])
            buffer.sort()
            if buffer == target:
                ret.append(i)
        return ret


    def findAnagrams(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: List[int]
            """
            length_s = len(s)
            length_p = len(p)
            if length_p > length_s:
                return []
            ret = []
            m1 = [0] * 26
            m2 = [0] * 26
            for index, c in enumerate(p):
                m1[ord(c) - 97] += 1
                # print(index)
                m2[ord(s[index]) - 97] += 1

            for i in range(len(s) - len(p) + 1):
                if m2 == m1:
                    ret.append(i)
                m2[ord(s[i]) - 97] -= 1
                if i == length_s - length_p:
                    break
                m2[ord(s[i + length_p]) - 97] += 1
            return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
