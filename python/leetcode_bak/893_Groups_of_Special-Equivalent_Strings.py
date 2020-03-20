# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def manager_string(self, s):
        even = []
        odd = []
        for index, c in enumerate(s):
            if index % 2 == 0:
                even.append(c)
            else:
                odd.append(c)
        even.sort()
        odd.sort()
        ret = ''
        for index, c in enumerate(even):
            ret += c
            try:
                ret += odd[index]
            except:
                pass
        return ret

    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m = set()
        for s in A:
            m.add(self.manager_string(s))
        return len(m)


def main():
    s = Solution()
    print(s.manager_string("edcba"))
    print(s.manager_string("dcba"))


if __name__ == "__main__":
    main()
