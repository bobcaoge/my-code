# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = list(senate)
        length = len(senate) + 1
        while len(senate) < length:
            length = len(senate)
            stack = []
            buff = []
            for c in senate:
                if not stack:
                    stack.append(c)
                else:
                    if c == stack[-1]:
                        stack.append(c)
                    else:
                        buff.append(stack.pop())
            stack.extend(buff)
            senate = stack

        return "Radiant" if senate[0] == 'R' else "Dire"


def main():
    s = Solution()
    print(s.predictPartyVictory("DRRDR"))



if __name__ == "__main__":
    main()
