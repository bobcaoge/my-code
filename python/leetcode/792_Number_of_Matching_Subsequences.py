# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def search(self, arr, i):
        if not arr:
            return -1
        start = 0
        end = len(arr)-1
        mid = int((start+end)/2)
        while start < end:
            if arr[mid] > i:
                end = mid
            else:
                start = mid+1
            mid = int((start+end)/2)
        return arr[start] if arr[start] > i else -1


    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        m = {}
        for i in range(26):
            m[chr(i+97)] = []
        for i, c in enumerate(S):
            m[c].append(i)

        def judge(word):
            i = -1
            for c in word:
                i = self.search(m[c], i)
                if i == -1:
                    return False
            return True
        ret = 0
        for word in words:
            ret += 1 if judge(word) else 0
        return ret


def main():
    s = Solution()
    print(s.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
    print(s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))


if __name__ == "__main__":
    main()
