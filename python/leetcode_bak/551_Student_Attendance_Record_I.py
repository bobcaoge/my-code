# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.find('A') != s.rfind('A'):
            return False
        l_record = 0
        for c in s:
            if c == 'L':
                l_record += 1
                if l_record == 3:
                    return False
            else:
                l_record = 0
        return True



def main():
    s = Solution()


if __name__ == "__main__":
    main()
