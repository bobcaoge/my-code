# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ret = []
        m = {}
        s = set()
        for word in words:
            m.clear()
            s.clear()
            for i, c in enumerate(word):
                if m.get(c, None) is not None:
                    if m[c] != pattern[i]:
                        break
                else:
                    if pattern[i] not in s:
                        m[c] = pattern[i]
                        s.add(pattern[i])
                    else:
                        break
            else:
                ret.append(word)
        return ret


def main():
    s = Solution()
    print(s.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))


if __name__ == "__main__":
    main()
