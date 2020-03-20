# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = [int(x) for x in version1.split(".") if x != ""]
        ver2 = [int(x) for x in version2.split(".") if x != ""]
        p1 = 0
        p2 = 0
        while p1 < len(ver1) or p2 < len(ver2):
            v1 = ver1[p1] if p1 < len(ver1) else 0
            v2 = ver2[p2] if p2 < len(ver2) else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            else:
                p1 += 1
                p2 += 1

        return 0

def main():
    s = Solution()
    print(s.compareVersion("0.1", "1.1"))
    print(s.compareVersion("1.0.1", "1"))
    print(s.compareVersion("7.5.2.4", "7.5.3"))
    print(s.compareVersion("1.01", "1.001"))
    print(s.compareVersion("1.0", "1.0.0"))


if __name__ == "__main__":
    main()
