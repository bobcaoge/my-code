# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def step(self, s):
        s_buffer = ""
        s_count = 0
        s_ret = ""
        index = 0
        length = len(s)

        while index < length:
            s_buffer = s[index]
            index += 1
            s_count = 1
            while index < length and s[index] == s_buffer[-1]:
                s_count += 1
                index += 1
            s_ret = s_ret + str(s_count) + s_buffer
        return s_ret




    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        buffer = ""
        for i in range(n):
            if i == 0:
                buffer = "1"
            else:
                buffer = self.step(buffer)
            print(buffer)
        return buffer




def main():
    s = Solution()
    # print(s.step("1112"))
    s.countAndSay(5)


if __name__ == "__main__":
    main()
