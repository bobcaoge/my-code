# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s = set(arr)
        if not arr:
            return False
        for i, num in enumerate(arr):
            if num == 0 :
                if arr.count(0) > 1:
                    return True
            elif num*2 in s:
                return True
        return False



def main():
    s = Solution()


if __name__ == "__main__":
    main()
