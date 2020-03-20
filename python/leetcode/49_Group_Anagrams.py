# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            # print(ret)
            m = [0]*26
            for c in s:
                m[ord(c)-97] += 1
            m = tuple(m)

            ret[m] = ret.get(m, [])+[s]
        return list(ret.values())
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            # print(ret)
            m = [0]*26
            for c in s:
                m[ord(c)-97] += 1
            m = hash(tuple(m))
            ret[m] = ret.get(m, [])+[s]
        return list(ret.values())

def main():
    s = Solution()
    print(s.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
