# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    record = 0
    def forword_find(self, s):
        """
        :type s: str
        """
        first = s[0]
        last_first = 0
        for c in s:
            if c == first:
                last_first += 1
            else:
                break
        ret = s[last_first:]
        record_another = 0
        for c in s[last_first:]:
            if c == str(1-int(first)):
                record_another += 1
                if last_first == record_another:
                    break
            else:
                break
        if last_first == record_another and last_first > 1:
            self.record += last_first
            return ret
        else:
            return None

    def back_find(self, s):
        """
        :type s: str
        """
        forward = s[0]
        back = str(1-int(forward))
        index_of_first_back = s.find(back)
        last_of_back = 0
        if index_of_first_back >= 0:
            sum_of_continuous_back = 0
            for c in s[index_of_first_back:]:
                if c == back:
                    last_of_back += 1
                else:
                    break
            if index_of_first_back >= last_of_back > 1:
                self.record += last_of_back
                return s[index_of_first_back:]
            else:
                self.record += 1
                return s[index_of_first_back:]
        else:
            return None

    def countBinarySubstrings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.record = 0
        forward = self.forword_find(s)
        if forward:
            back = None
        else:
            back = self.back_find(s)
        while forward or back:
            s = forward or back
            forward = self.forword_find(s)
            if forward:
                back = None
            else:
                back = self.back_find(s)
        return self.record
    def countBinarySubstrings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = 0
        while s:
            forward = s[0]
            back = str(1-int(forward))
            last_of_forward = s.find(back)
            if last_of_forward == -1:
                break
            last_of_back = 0
            for c in s[last_of_forward:]:
                if c == back:
                    last_of_back += 1
                else:
                    break
            if last_of_forward > last_of_back:
                record += last_of_back
            else:
                record += last_of_forward
            s = s[last_of_forward:]
        return record
    def countBinarySubstrings3(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = 0
        first = 0
        second = 1
        i = 1
        while i < len(s):
            # print(first)
            if s[i] == s[i-1]:
                second += 1
            else:
                record += min(first, second)
                first = second
                second = 1
            i += 1
        record += min(first, second)
        return record

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = 0
        first = 0
        second = 1

        for i in range(1, len(s)):
            # print(first)
            if s[i] == s[i - 1]:
                second += 1
            else:
                record += min(first, second)
                first = second
                second = 1
        return record + min(first, second)



def main():
    s = Solution()
    print(s.countBinarySubstrings("00110011"))
    print(s.countBinarySubstrings("10101"))
    print(s.countBinarySubstrings("000111000"))
    print(s.countBinarySubstrings("11110011"))


if __name__ == "__main__":
    main()
