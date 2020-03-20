# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def judge(query, pattern):
            i = 0
            j = 0
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    j += 1
                else:
                    if "A" <= query[i] <= "Z":
                        return False
                i += 1
            if j < len(pattern):
                return False
            for index in range(i, len(query)):
                if "A" <= query[index] <= "Z":
                    return False
            return j == len(pattern)
        return [judge(q, pattern) for q in queries]


def main():
    s = Solution()
    print(s.camelMatch( queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))


if __name__ == "__main__":
    main()
