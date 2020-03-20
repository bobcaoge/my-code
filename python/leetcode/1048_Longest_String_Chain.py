# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, lambda x, y : 1 if len(x) > len(y) else -1)
        # print(words)
        dp = [1]*len(words)
        for i in range(len(words)):
            for j in range(i-1, -1, -1):
                if len(words[i]) - len(words[j]) == 2:
                    break
                if self.is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    def is_predecessor(self, s1, s2):
        """
        judge that if s2 is the predecessor of s1
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) != len(s1) + 1:
            return False
        for i in range(len(s2)):
            if s1 == s2[:i] + s2[i+1:]:
                return True


def main():
    s = Solution()
    print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))
    print(s.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))


if __name__ == "__main__":
    main()
