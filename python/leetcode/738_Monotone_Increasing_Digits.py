# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N
        s = str(N)
        pre = ""
        pos = -1
        for i in range(1, len(s)):
            if s[i] >= s[i-1]:
                pre += s[i-1]
            else:
                pos = i-1
                break
        if pos == -1:
            return N
        end = "9"*(len(s)-pos-1)
        cur = str(int(s[pos])-1)
        for i in range(pos-1, -1, -1):
            if s[i] <= cur:
                return int(s[:i+1]+cur+end)
            else:
                end += "9"
                cur = str(int(s[i])-1)
        end = "9"*(len(s)-1)
        cur = str(int(s[0])-1)
        return int((cur if cur != "0" else "")+end)







def main():
    s = Solution()
    print(s.monotoneIncreasingDigits(668841))
    print(s.monotoneIncreasingDigits(1234))
    print(s.monotoneIncreasingDigits(10))
    print(s.monotoneIncreasingDigits(234679643))


if __name__ == "__main__":
    main()
