# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import copy

class Solution(object):

    def get_hour_1(self, A):
        if 2 in A:
            hour = "2"
            A.remove(2)
            a = {0,1,2,3} & set(A)
            if a:
                hour += str(max(a))
                A.remove(max(a))
                return hour
            else:
                A.append(2)
    def get_hour_2(self, A):
        if 1 in A:
            hour = "1"
            A.remove(1)
            a = {0,1,2,3,4,5,6,7,8,9} & set(A)
            if a:
                hour += str(max(a))
                A.remove(max(a))
                return hour
            else:
                A.append(1)
    def get_hour_3(self, A):
        if 0 in A:
            hour = "0"
            A.remove(0)
            a = {0,1,2,3,4,5,6,7,8,9} & set(A)
            if a:
                hour += str(max(a))
                A.remove(max(a))
                return hour
            else:
                A.append(0)
    def get_minute(self, A):
        a = {0,1,2,3,4,5} & set(A)
        if a:
            minute = str(max(a))
            A.remove(max(a))
            minute += str(A[0])
            return minute

    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        bak = copy.deepcopy(A)
        hour = self.get_hour_1(A)
        if hour:
            minute = self.get_minute(A)
            if minute:
                return hour+":"+minute
        B = copy.deepcopy(bak)
        hour = self.get_hour_2(B)
        if hour:
            minute = self.get_minute(B)
            if minute:
                return hour+":"+minute
        B = copy.deepcopy(bak)
        hour = self.get_hour_3(B)
        if hour:
            minute = self.get_minute(B)
            if minute:
                return hour+":"+minute
        return ""






def main():
    s = Solution()
    print(s.largestTimeFromDigits([1,2,3,4]))
    print(s.largestTimeFromDigits([5,5,5,5]))
    print(s.largestTimeFromDigits([2,0,6,6]))


if __name__ == "__main__":
    main()
