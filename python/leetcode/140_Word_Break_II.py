# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def judge(s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: bool
            """
            monitor = [False]*len(s)
            for i in range(len(s)):
                for word in wordDict:
                    if word == s[i-len(word)+1:i+1] and (monitor[i-len(word)] or i-len(word) == -1):
                        monitor[i] = True
            return monitor[-1]
        if not judge(s, wordDict):
            return []
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = [""]
        for i, c in enumerate(s):
            for j in range(i+1):
                if s[j:i+1] in wordDict and dp[j]:
                    dp[i+1].extend([x+" "+s[j:i+1] for x in dp[j]])
        return [x[1:] for x in dp[-1]] if dp[-1] else []



def main():
    s = Solution()
    print(s.wordBreak(s = "catsanddog",
    wordDict = ["cat", "cats", "and", "sand", "dog"]))
    print(s.wordBreak('a', ['a']))
    print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                     , ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))



if __name__ == "__main__":
    main()
