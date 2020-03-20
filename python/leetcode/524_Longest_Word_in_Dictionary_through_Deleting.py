# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def judge(source, target):
            index_of_src = 0
            index_of_tar = 0
            while index_of_src < len(source) and index_of_tar < len(target):
                if source[index_of_src] == target[index_of_tar]:
                    index_of_tar += 1
                index_of_src += 1
            return index_of_tar == len(target)
        # print(judge(s, "ewafeffewafewf"))
        ret = ""
        for word in d:
            if judge(s, word) and (len(word) > len(ret) or len(word) == len(ret) and word < ret):
                ret = word
        return ret


def main():
    s = Solution()
    print(s.findLongestWord("aewfafwafjlwajflwajflwafj",
                            ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]))


if __name__ == "__main__":
    main()
