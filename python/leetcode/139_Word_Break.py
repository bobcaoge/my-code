# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def wordBreak(self, s, wordDict):
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



def main():
    s = Solution()
    print(s.wordBreak("bb", ["a","b","bbb","bbbb"]))
    print(s.wordBreak("leetCode", ["leet", "Code"]))
    print(s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
    print(s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))

if __name__ == "__main__":
    main()
