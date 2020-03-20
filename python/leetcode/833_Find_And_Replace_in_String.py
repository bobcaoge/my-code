# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        info = [[indexes[i], i] for i in range(len(indexes))]
        info.sort()
        before = 0
        ret = ""
        for i, index in enumerate(info):
            index = index[0]
            if S[index:index+len(sources[info[i][1]])] == sources[info[i][1]]:
                ret += S[before:index] + targets[info[i][1]]
                before = index+len(sources[info[i][1]])
        ret += S[before:len(S)]
        return ret


def main():
    s = Solution()
    print(s.findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]))
    print(s.findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]))
    print(s.findReplaceString("vmokgggqzp",
                              [3,5,1],
                              ["kg","ggq","mo"],
                              ["s","so","bfr"]))

if __name__ == "__main__":
    main()
