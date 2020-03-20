# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def nextGreatestLetter1(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ret = 'zz'
        for letter in letters:
            if letter > target:
                ret = min(letter, ret)
        return ret if ret != 'zz' else min(letters)
    def nextGreatestLetter2(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]:
            return letters[0]
        start = 0
        end = len(letters) - 1
        mid = int((end + start) / 2)
        while start < end:
            if letters[mid] > target:
                end = mid
                mid = int((end + start) / 2)
            else:
                start = mid + 1
                mid = int((end + start) / 2)

        if letters[mid] == target:
            return letters[(mid+1)%len(letters)]
        else:
            return letters[mid]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
