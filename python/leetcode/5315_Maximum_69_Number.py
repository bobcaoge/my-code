# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        ret = ''
        for i, c in enumerate(num):
            if c == '6':
                return int(ret+'9'+num[i+1:])
            ret += '9'
        return int(num)





def main():
    s = Solution()


if __name__ == "__main__":
    main()
