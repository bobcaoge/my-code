# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ret = -1
        for i in range(len(strs)):
            for j in range(len(strs)):
                if j != i and self.judge(strs[i], strs[j]) :
                    break
            else:
                ret = max(ret, len(strs[i]))
            # print(ret)
        return ret

    def judge(self, s1, s2):
        """
        if s1 is a subsequence of s2
        :param s1:
        :param s2:
        :return:
        """
        if len(s2) < len(s1):
            return False
        index_of_s1 = 0
        index_of_s2 = 0
        while index_of_s1 < len(s1) and index_of_s2 < len(s2):
            if s1[index_of_s1] == s2[index_of_s2]:
                index_of_s1 += 1
                index_of_s2 += 1
            else:
                index_of_s2 += 1
        return True if index_of_s1 == len(s1) else False


def main():
    s = Solution()
    print(s.findLUSlength(["aba", "aba", "a"]))
    print(s.findLUSlength(["aabbcc", "aabbcc","cb"]))


if __name__ == "__main__":
    main()
