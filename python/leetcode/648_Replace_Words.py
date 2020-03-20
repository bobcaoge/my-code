# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def replaceWords(self, roots, sentence):
        """
        :type roots: List[str]
        :type sentence: str
        :rtype: str
        """
        s = set(roots)
        words = sentence.split(" ")
        ret = []
        for i, word in enumerate(words):
            for j in range(1, len(word)+1):
                if word[:j] in s:
                    ret.append(word[:j])
                    break
            else:
                ret.append(word)
        return " ".join(ret)


def main():
    s = Solution()
    print(s.replaceWords(["cat", "bat", "rat"],
    "the cattle was rattled by the battery"))


if __name__ == "__main__":
    main()
