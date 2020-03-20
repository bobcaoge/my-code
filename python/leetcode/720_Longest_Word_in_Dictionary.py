# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        words += ["z"]
        stack = []
        ret = ""
        length_ret = 0
        for i in range(len(words)):
            # print(stack)
            s = words[i]
            length_s = len(s)
            if length_s == 1:
                if stack and len(stack[-1]) > length_ret:
                    ret = stack[-1]
                    length_ret = len(ret)
                stack = [words[i]]
            else:
                if stack and len(stack[-1]) > length_ret:
                    ret = stack[-1]
                stack = stack[:length_s-1]
                if stack and s[:-1] == stack[-1]:
                    stack.append(s)
        return ret


    def longestWord2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        words += ["z"]
        stack = []
        ret = ""
        for i in range(len(words)):
            # print(stack)
            s = words[i]
            if len(s) == 1:
                if stack and len(stack[-1]) > len(ret):
                    ret = stack[-1]
                stack = [words[i]]
            else:
                if stack and len(stack[-1]) > len(ret):
                    ret = stack[-1]
                stack = stack[:len(s)-1]
                if stack and s[:-1] == stack[-1]:
                    stack.append(s)
        return ret


    def longestWord1(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        words += [""]
        stack = []
        ret = ""
        for i in range(len(words)):
            # print(stack)
            s = words[i]
            if len(s) == 1:
                if stack and len(stack[-1]) > len(ret):
                    ret = stack[-1]
                stack = [words[i]]
            else:
                if stack and len(stack[-1]) > len(ret):
                    ret = stack[-1]
                while stack and len(stack[-1]) >= len(s):
                    stack.pop()
                if stack and s[:-1] == stack[-1]:
                    stack.append(s)
        return ret








def main():
    s = Solution()
    # print(s.longestWord(["a",  "app", "appl", "ap", "apply", "apple", "b", "ba",
    #                       "ban", "bana"]))
    # print(s.longestWord(["n","j","sl","yyd","slo","jk","jkdt","y","yy"]))

    print(s.longestWord(["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd", "racyc"]))


if __name__ == "__main__":
    main()
