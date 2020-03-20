# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ret = 0
        words = [[x, set(x)] for x in words]
        print(words)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (words[i][1] & words[j][1]):
                    ret = max(len(words[i][0])*len(words[j][0]), ret)
        return ret



def main():
    s = Solution()
    print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))


if __name__ == "__main__":
    main()
