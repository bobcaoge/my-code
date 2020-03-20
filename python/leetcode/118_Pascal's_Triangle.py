# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return[[1],[1,1]]
        else:
            last_ret = [[1],[1,1]]
            for i in range(numRows-2):
                index = 0
                newline =[1]
                while index < len(last_ret[-1]) - 1:
                    newline.append(last_ret[-1][index]+last_ret[-1][index+1])
                    index += 1
                newline.append(1)
                last_ret.append(newline)
            return last_ret



def main():
    s = Solution()
    for i in range(1,6):
        print(s.generate(i))


if __name__ == "__main__":
    main()
