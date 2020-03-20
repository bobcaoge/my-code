# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        m = collections.Counter(text)
        target ={
            'b':1,
            'a':1,
            'l':2,
            'o':2,
            'n':1
        }
        return min([m[letter]//num for letter, num in target.items()])



def main():
    s = Solution()


if __name__ == "__main__":
    main()
