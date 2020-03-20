# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        record = [0]*26
        for c in s1:
            record[ord(c)-97] += 1
        buff = [0]*26
        for index,c in enumerate(s2):
            if index < len(s1):
                buff[ord(c)-97] += 1
            else:
                if record == buff:
                    return True
                buff[ord(c)-97] += 1
                buff[ord(s2[index-len(s1)])-97] -= 1
        return buff == record


def main():
    s = Solution()
    print(s.checkInclusion(s1 = "ab",s2 = "eidbaooo"))


if __name__ == "__main__":
    main()
