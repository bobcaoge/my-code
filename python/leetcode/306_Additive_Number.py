# /usr/bin/python3.6
# -*- coding:utf-8 -*-



class Solution(object):
    flag = False
    def recursion(self, first, num):
        """
        :type first: str
        :type num: str
        """
        length_of_first = len(first)
        first = int(first)
        if not num:
            return
        for i in range(len(num)-length_of_first+1):
            second = int(num[:i+1])
            if i > 0 and num[0] == "0":
                return
            # print(first, second)
            sum_ = str(first+second)
            if num[i+1:].startswith(sum_):
                length = len(sum_) + i+1
                if length == len(num):
                    print(first, num[:i+1], sum_, num)
                    self.flag = True
                else:
                    self.recursion(str(second), num[i+1:])


    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return False
        self.flag = False
        for i in range(int(len(num)/2)+1):
            first = num[:i+1]
            # print(first)
            if i > 0 and num[0] == "0":
                break
            if not self.flag:
                self.recursion(first, num[i+1:])
        return self.flag

def main():
    s = Solution()
    print("0235813")
    print(s.isAdditiveNumber("1023"))
    print(s.isAdditiveNumber("100200300"))
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("365464134684763546843"))
    print(s.isAdditiveNumber("101"))
    print(s.isAdditiveNumber("101010101010101"))


if __name__ == "__main__":
    main()
