# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return[1, 1]
        else:
            last_ret = [1, 1]
            newline = None
            for i in range(rowIndex-1):
                index = 0
                newline =[1]
                while index < len(last_ret) - 1:
                    newline.append(last_ret[index]+last_ret[index+1])
                    index += 1
                newline.append(1)
                last_ret = newline
            return last_ret

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return[1, 1]
        else:
            last_ret = [0 for i in range(rowIndex+1)]
            last_ret[0] = 1
            last_ret[1] = 1

            # print(last_ret)
            buffer = 0
            newline = [0 for i in range(rowIndex+1)]
            newline[0] = 1
            for i in range(rowIndex-1):
                index = 0
                while index < i + 2 :
                    newline[index+1] = last_ret[index]+last_ret[index+1]
                    index += 1
                newline[index] = 1
                for j in range(rowIndex+1):
                    buffer = last_ret[j]
                    last_ret[j] =  newline[j]
                    newline[j] = buffer
            return last_ret




def main():
    s = Solution()
    for i in range(0,6):
        print(s.getRow(i))

if __name__ == "__main__":
    main()
