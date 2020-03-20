# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def manage(self, cur, ret, k):
        if not ret:
            return cur, 0
        length = len(ret)
        i = 0
        pos = length

        index = length-i-1
        while k > 0 and 0 <= index < length:
            if ret[index] > cur:
                k -= 1
                pos = index
            i += 1
            index = length-i-1
        return ret[:pos] + cur, length-pos

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        keep = k
        if not num:
            return num
        # if len(num) == k:
        #     return ""
        i = 0
        ret = ""
        while k > 0 and i < len(num):
            # print(ret)
            ret, removed = self.manage(num[i], ret, k)
            k -= removed
            i += 1

        pos_first_char_which_is_not_zera = len(ret)
        ret = ret+num[i:]
        i = 0
        while i < len(ret):
            if ret[i] != "0":
                pos_first_char_which_is_not_zera = i
                break
            i += 1
        if pos_first_char_which_is_not_zera == len(ret):
            return "0"
        ret = ret[pos_first_char_which_is_not_zera:][:len(num)-keep]

        return ret if ret else "0"




def main():
    s = Solution()
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("13141517", 3))
    print(s.removeKdigits("10", 2))
    print(s.removeKdigits("10200", 1))
    print(s.removeKdigits("111111999", 4))


if __name__ == "__main__":
    main()
