# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = None

    def buffer(self, s, last, ans):
        """
        :type s: str
        :type last:int
        :type ans: str
        :rtype
        """

        if last == 0 :
            if not s:
                self.ret.add(ans[1:])
        else:
            if s and len(s) >= last:
                if s[0] == "0":
                    self.buffer(s[1:], last-1, ans+".0")
                else:
                    for i in range(1, 4):
                        if int(s[:i]) < 256:
                            self.buffer(s[i:], last-1, ans+"."+s[:i])

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ret = set()
        self.buffer(s, 4, "")
        return list(self.ret)


def main():
    s = Solution()
    # print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("0000"))
    print(s.restoreIpAddresses("255000"))
    print(s.restoreIpAddresses("000255"))
    print(s.restoreIpAddresses("002550"))
    print(s.restoreIpAddresses("1111"))
    print(s.restoreIpAddresses("19216811"))


if __name__ == "__main__":
    main()
