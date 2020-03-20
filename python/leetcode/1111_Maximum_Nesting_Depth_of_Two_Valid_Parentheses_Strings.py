# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ret = [0]*len(seq)
        num = 0
        for i in range(len(seq)):
            if seq[i] == "(":
                num += 1
                if num % 2 == 0:
                    ret[i] = 1
            else:
                if num % 2 == 0 and num != 0:
                    ret[i] = 1
                num -= 1
        return ret






def main():
    s = Solution()
    print(s.maxDepthAfterSplit("(()(()))"))
    print(s.maxDepthAfterSplit("(()())"))


if __name__ == "__main__":
    main()
