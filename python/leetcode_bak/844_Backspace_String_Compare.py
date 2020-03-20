# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_list = []
        for s in S:
            if s == "#":
                try:
                    s_list.pop()
                except:
                    pass
            else:
                s_list.append(s)
        t_list = []
        for s in T:
            if s == "#":
                try:
                    t_list.pop()
                except:
                    pass
            else:
                t_list.append(s)
        return s_list == t_list


def main():
    s = Solution()


if __name__ == "__main__":
    main()
