# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in s:
            if not stack:
                stack.append([c, 1])
            else:
                if c == stack[-1][0]:
                    if stack[-1][1] == k-1:
                        stack[-k+1:] = []
                    else:
                        stack.append([c, stack[-1][1]+1])
                else:
                    stack.append([c, 1])
        return "".join([x[0] for x in stack])


def main():
    s = Solution()
    print(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
    print(s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))


if __name__ == "__main__":
    main()
